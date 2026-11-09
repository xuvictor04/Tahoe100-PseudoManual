---
symbol: "SCD5"
type: "gene"
col: 6971
ensembl_id: "ENSG00000145284"
name: "stearoyl-CoA desaturase 5"
location: "4q21.22"
module: 115
arm: "+"
pooled_cpm: 30.62
n_lines_expressing: 40
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SCD5

*stearoyl-CoA desaturase 5* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +14.8, q 0e+00, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.417× (z -17.3, q 0e+00, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC47A1]] (+0.66, fdr 1e-05), [[PARD6G]] (+0.66, fdr 7e-06), [[MSI1]] (+0.61, fdr 1e-05); moves opposite to [[WASHC4]] (-0.51, fdr 4e-05), [[RSPH3]] (-0.46, fdr 1e-04), [[CCDC191]] (-0.44, fdr 3e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00937]] → it (grade B ⚠); 6 go from it, the strongest it → [[FHL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +14.8 | 0e+00 | 28/38 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +14.4 | 2e-44 | 32/38 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +9.5 | 2e-19 | 23/38 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +8.2 | 3e-14 | 27/37 (SW480, A-427, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +8.2 | 3e-14 | 19/37 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +6.7 | 2e-09 | 17/38 (LoVo, J82, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.35×** | +6.3 | 3e-08 | 16/37 (A549, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 3e-07 | 18/37 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.8 | 3e-07 | 21/38 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 4e-04 | 12/38 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.2 | 0.001 | 12/35 (HOP62, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.003 | 9/37 (HOP62, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.41×** | +3.7 | 0.008 | 11/32 (HOP62, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.032 | 7/37 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | 1.18× | +3.2 | 0.045 | 8/29 (Hs 766T, NCI-H1792, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.081 | 4/38 (A-427, SW480, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.095 | 5/35 (SW1417, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.417×** | -17.3 | 0e+00 | 33/38 (AN3 CA, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.639×** | -13.1 | 1e-36 | 25/38 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -12.2 | 4e-32 | 26/38 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -11.6 | 4e-29 | 28/38 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -11.1 | 1e-26 | 26/38 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -9.6 | 1e-19 | 25/37 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -6.8 | 6e-10 | 22/37 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.735×** | -6.3 | 2e-08 | 18/37 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -6.1 | 7e-08 | 17/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.766×** | -5.5 | 2e-06 | 15/37 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.686×** | -4.1 | 0.003 | 12/38 (NCI-H1792, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.871× | -4.0 | 0.003 | 12/38 (BT-474, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.037 | 9/38 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.840× | -3.3 | 0.037 | 12/36 (AN3 CA, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 70.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -19.5) |
| [[A-172 (line)]] | wt | 53.2 | 2 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.88× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -18.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.295× (z -12.1) |
| [[LoVo (line)]] | wt | 86.0 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.9) ⚠ cell-cycle shift, explains ~48% of this change | [[Harringtonine (drug)]] 5 µM 0.415× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 17.7 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.5) | [[Harringtonine (drug)]] 0.5 µM 0.133× (z -15.9) |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -10.9) |
| [[HOP62 (line)]] | alt | 11.0 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.68× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 85.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -17.8) |
| [[RKO (line)]] | wt | 128 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -14.0) |
| [[J82 (line)]] | alt | 32.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.22× (z +10.1) | [[Digitoxin (drug)]] 0.05 µM 0.154× (z -9.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0800× (z -22.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.8 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.428× (z -9.6) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0682× (z -15.1) |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -13.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW48 (line)]] | wt | 52.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.7) |
| [[A549 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 1 | — | [[Rimonabant (drug)]] 0.5 µM 0.0630× (z -8.6) |
| [[HCT15 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HS-578T (line)]] | alt | 9.06 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0938× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.230× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC47A1]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PARD6G]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[MSI1]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PTK7]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.57 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[ARHGAP44]] | +0.57 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[CRACD]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GPC4]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[ARHGEF26]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[FAXC]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CACNB4]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[RBPMS2]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC4]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[RSPH3]] | -0.46 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[CCDC191]] | -0.44 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[DNAL4]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[RAB3GAP2]] | -0.44 | -0.48 / -0.29 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00937]] | B | LINC00937 activity raises SCD5's level | lines that do not express LINC00937 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without LINC00937 | 0.035 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000255367, MRAS; maybe low, not absent |
| [[CACNB4]] | B | CACNB4 activity raises SCD5's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 3.53× lower at baseline in the lines without CACNB4 | 0.039 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[TMEM150C]] | B | TMEM150C activity raises SCD5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without TMEM150C | 0.050 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[CCDC136]] | B | CCDC136 activity raises SCD5's level | lines that do not express CCDC136 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without CCDC136 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent |
| [[ASIC1]] | C | ASIC1 activity raises SCD5's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 5.95× lower at baseline in the lines without ASIC1 | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHL1]] | B | SCD5 activity raises FHL1's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 3.69× lower at baseline in the lines without SCD5 | 0.026 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[RAB6B]] | B | SCD5 activity raises RAB6B's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without SCD5 | 0.048 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[OTULINL]] | B | SCD5 activity lowers OTULINL's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without SCD5 | 0.060 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[RHBDL3]] | B | SCD5 activity raises RHBDL3's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without SCD5 | 0.074 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[TUB]] | B | SCD5 activity raises TUB's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without SCD5 | 0.097 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[SMO]] | B | SCD5 activity raises SMO's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.08× lower at baseline in the lines without SCD5 | 0.097 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.7, 38.2); signed map (-22.5, 36.3). **Vector** length 92.7, 21.3% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +14.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.4 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | stearoyl-CoA desaturase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,629,539-82,798,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACOD4, FLJ21032, FADS4, HSCD5; previously SCD4 |
| Gene groups (HGNC) | Fatty acid desaturases; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Fatty acyl-CoA biosynthesis; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SK9](https://www.uniprot.org/uniprotkb/Q86SK9) (Stearoyl-CoA desaturase 5):

> Stearoyl-CoA desaturase that utilizes O(2) and electrons from reduced cytochrome b5 to introduce the first double bond into saturated fatty acyl-CoA substrates. Catalyzes the insertion of a cis double bond at the delta-9 position into fatty acyl-CoA substrates including palmitoyl-CoA and stearoyl-CoA. Gives rise to a mixture of 16:1 and 18:1 unsaturated fatty acids. Involved in neuronal cell proliferation and differentiation through down-regulation of EGFR/AKT/MAPK and Wnt signaling pathways.

**Summary**, from NCBI Gene [79966](https://www.ncbi.nlm.nih.gov/gene/79966):

> Stearoyl-CoA desaturase (SCD; EC 1.14.99.5) is an integral membrane protein of the endoplasmic reticulum that catalyzes the formation of monounsaturated fatty acids from saturated fatty acids. SCD may be a key regulator of energy metabolism with a role in obesity and dislipidemia. Four SCD isoforms, Scd1 through Scd4, have been identified in mouse. In contrast, only 2 SCD isoforms, SCD1 (MIM 604031) and SCD5, have been identified in human. SCD1 shares about 85% amino acid identity with all 4 …

**Accessions** — [HGNC:21088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21088) · Entrez [79966](https://www.ncbi.nlm.nih.gov/gene/79966) · UniProt [Q86SK9](https://www.uniprot.org/uniprotkb/Q86SK9) · Ensembl [ENSG00000145284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145284)

## Data

Gene col 6971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6971); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6971]; `tensor/DDL_lfc|DDL_z.npy` [6971]; `embed/gene_vectors.npy` [6971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6971 or target_col == 6971). Every well: [[SCD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
