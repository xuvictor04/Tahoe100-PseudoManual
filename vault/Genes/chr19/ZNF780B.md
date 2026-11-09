---
symbol: "ZNF780B"
type: "gene"
col: 4856
ensembl_id: "ENSG00000128000"
name: "zinc finger protein 780B"
location: "19q13.2"
module: 16
arm: "+"
pooled_cpm: 67.55
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF780B

*zinc finger protein 780B* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +7.6, q 2e-11, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.40× (z +6.1, q 3e-07, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.496× (z -12.7, q 3e-34, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF283]] (+0.67, fdr 1e-05), [[ZNF780A]] (+0.65, fdr 7e-06, ⚠ same locus), [[ZNF594]] (+0.61, fdr 7e-06), [[ZNF268]] (+0.60, fdr 3e-05); moves opposite to [[RELL1]] (-0.64, fdr 1e-05), [[SETD3]] (-0.56, fdr 2e-05), [[MTM1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01535]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +7.6 | 2e-11 | 30/46 (LS 180, HT-29, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +6.1 | 3e-07 | 25/46 (RKO, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.5 | 6e-06 | 25/46 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.33×** | +5.3 | 2e-05 | 24/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.5 | 9e-04 | 20/46 (A498, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +3.9 | 0.008 | 16/46 (KATO III, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.034 | 12/45 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.034 | 15/45 (SW480, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.056 | 16/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.056 | 16/46 (KATO III, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +3.3 | 0.056 | 13/37 (LS 180, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -12.7 | 3e-34 | 42/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -11.9 | 4e-30 | 36/45 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -9.1 | 2e-17 | 35/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.668×** | -7.3 | 4e-11 | 30/46 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.684×** | -6.6 | 5e-09 | 31/45 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -6.4 | 2e-08 | 29/46 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.705×** | -6.1 | 1e-07 | 25/46 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.752×** | -5.2 | 2e-05 | 22/46 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.765×** | -4.8 | 9e-05 | 20/44 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -4.3 | 8e-04 | 18/46 (NCI-H23, SNU-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.778×** | -4.2 | 0.002 | 21/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.797×** | -4.1 | 0.002 | 21/46 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.802×** | -4.0 | 0.003 | 14/46 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.8 | 0.007 | 0/47 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.041 | 9/46 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.061 | 11/45 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 588 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -23.9) |
| [[HT-29 (line)]] | alt | 58.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -9.4) |
| [[SW480 (line)]] | alt | 53.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -12.5) |
| [[COLO 205 (line)]] | alt | 51.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 35.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +22.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.183× (z -13.3) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 59.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.4) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -14.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0864× (z -13.0) |
| [[J82 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.372× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 45.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -10.8) |
| [[LoVo (line)]] | wt | 27.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.321× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.399× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H661 (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.139× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[RKO (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SHP-77 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF283]] | +0.67 | +0.54 / +0.73 | both halves | 1e-05 | same gene group |
| [[ZNF780A]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 | same gene group; ⚠ same locus (12.9 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF594]] | +0.61 | +0.70 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZNF268]] | +0.60 | +0.69 / +0.46 | both halves | 3e-05 | same gene group |
| [[ZNF585B]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | same gene group |
| [[ZNF383]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[XKR6]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZKSCAN4]] | +0.59 | +0.61 / +0.57 | both halves | 9e-06 | same gene group |
| [[ZNF528]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 | same gene group |
| [[ZSCAN20]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 | same gene group |
| [[ZNF444]] | +0.58 | +0.30 / +0.63 | both halves | 2e-04 | same gene group |
| [[ZNF573]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 | same gene group |
| [[LINC01535]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.64 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[SETD3]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[MTM1]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ZFYVE21]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RUSC1]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GIT1]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[FBH1]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[NAA80]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ATP11B]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01535]] | B | LINC01535 activity raises ZNF780B's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without LINC01535 | 0.017 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.4, 14.1); signed map (2.0, -27.5). **Vector** length 71.7, 13.7% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.2 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.9 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -2.3 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 780B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,028,260-40,056,231 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF779 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6R6](https://www.uniprot.org/uniprotkb/Q9Y6R6) (Zinc finger protein 780B):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [163131](https://www.ncbi.nlm.nih.gov/gene/163131):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33109) · Entrez [163131](https://www.ncbi.nlm.nih.gov/gene/163131) · UniProt [Q9Y6R6](https://www.uniprot.org/uniprotkb/Q9Y6R6) · Ensembl [ENSG00000128000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128000)

## Data

Gene col 4856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4856); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4856]; `tensor/DDL_lfc|DDL_z.npy` [4856]; `embed/gene_vectors.npy` [4856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4856 or target_col == 4856). Every well: [[ZNF780B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF780B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
