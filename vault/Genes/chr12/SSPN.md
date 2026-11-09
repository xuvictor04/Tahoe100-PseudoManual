---
symbol: "SSPN"
type: "gene"
col: 4400
ensembl_id: "ENSG00000123096"
name: "sarcospan"
location: "12p12.1"
module: 80
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 35
n_dd_up: 20
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SSPN

*sarcospan* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.84× (z +35.0, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.487× (z -10.1, q 3e-21, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP2]] (+0.71, fdr 4e-05), [[SEPTIN7-DT]] (+0.68, fdr 5e-05), [[TMEM202-AS1]] (+0.67, fdr 3e-05); moves opposite to [[HERC2P2]] (-0.63, fdr 1e-04), [[HERC2P9]] (-0.62, fdr 3e-05), [[WRAP73]] (-0.61, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAGI2-AS3]] → it (grade B ⚠); 11 go from it, the strongest it → [[TMEM202-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.84×** | +35.0 | 0e+00 | 29/29 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +15.2 | 0e+00 | 17/30 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +13.3 | 3e-38 | 9/14 (NCI-H460, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +12.9 | 7e-36 | 18/24 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +12.6 | 3e-34 | 13/17 (SW 900, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +8.4 | 4e-15 | 22/30 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.1 | 3e-14 | 13/29 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +7.9 | 3e-13 | 20/31 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.2 | 4e-11 | 10/29 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.3 | 1e-08 | 14/32 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.9 | 2e-07 | 12/32 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 12/33 (NCI-H1573, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.3 | 7e-04 | 4/15 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 9e-04 | 9/31 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.001 | 9/30 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.016 | 6/32 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.019 | 3/32 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.070 | 5/31 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.075 | 9/30 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -10.1 | 3e-21 | 22/31 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -7.6 | 1e-11 | 19/32 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -6.2 | 9e-08 | 17/31 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -6.2 | 9e-08 | 15/33 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -4.4 | 0.001 | 17/27 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -4.3 | 0.001 | 12/32 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -4.1 | 0.004 | 10/31 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.0 | 0.004 | 14/31 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.753×** | -4.0 | 0.005 | 9/31 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.758×** | -3.9 | 0.006 | 7/31 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.779×** | -3.5 | 0.024 | 16/29 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -3.4 | 0.038 | 11/32 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.072 | 8/31 (hTERT-HPNE, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.7 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -14.8) |
| [[PANC-1 (line)]] | alt | 25.4 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.254× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -10.1) |
| [[LoVo (line)]] | wt | 8.36 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.0487× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 8.30 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +13.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0968× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 7.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +13.9) | — |
| [[A498 (line)]] | wt | 3.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 22.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +11.7) | — |
| [[C32 (line)]] | wt | 6.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 5.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 4.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +8.6) | — |
| [[J82 (line)]] | alt | 5.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +8.6) | — |
| [[KATO III (line)]] | alt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.173× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 9.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | +0.71 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[SEPTIN7-DT]] | +0.68 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | +0.67 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[TGFB3]] | +0.67 | +0.49 / +0.51 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[LINC01135]] | +0.67 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | +0.67 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[F8]] | +0.67 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.67 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[WAKMAR2]] | +0.66 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LPXN]] | +0.66 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[ERCC6L2-AS1]] | +0.66 | +0.57 / +0.27 | both halves | 3e-04 |  |
| [[SGO1-AS1]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P2]] | -0.63 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[HERC2P9]] | -0.62 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[WRAP73]] | -0.61 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.60 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[TRABD]] | -0.60 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[SLC9A6]] | -0.60 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[BRF1]] | -0.59 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[LRRC42]] | -0.59 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[L2HGDH]] | -0.59 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGI2-AS3]] | B | MAGI2-AS3 activity raises SSPN's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without MAGI2-AS3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[LINC01358]] | B | LINC01358 activity raises SSPN's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without LINC01358 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |
| [[MATN2]] | B | MATN2 activity raises SSPN's level | lines that do not express MATN2 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without MATN2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, NAT14, KIF17; maybe low, not absent |
| [[JAM2]] | C | JAM2 activity raises SSPN's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without JAM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; co-absent with the target |
| [[FGF12]] | C | FGF12 activity raises SSPN's level | lines that do not express FGF12 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without FGF12 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM182B, ENSG00000261341, WDR35; maybe low, not absent |
| [[SYNPO]] | C | SYNPO activity raises SSPN's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without SYNPO | 0.089 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM202-AS1]] | B | SSPN activity raises TMEM202-AS1's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without SSPN | 0.045 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[RIPK2-DT]] | B | SSPN activity raises RIPK2-DT's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without SSPN | 0.052 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| cells under [[Naproxen (drug)]] 5 µM | B | SSPN activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 0.86× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[PRECSIT]] | B | SSPN activity raises PRECSIT's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without SSPN | 0.058 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[PATL2]] | B | SSPN activity raises PATL2's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without SSPN | 0.060 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | SSPN activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 0.85× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[LINC02955]] | B | SSPN activity raises LINC02955's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without SSPN | 0.085 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| cells under [[Ferulic acid (drug)]] 0.5 µM | B | SSPN activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 1.31× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| cells under [[Doxycycline (monohydrate) (drug)]] 0.5 µM | B | SSPN activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 1.26× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[B3GNT9]] | B | SSPN activity raises B3GNT9's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without SSPN | 0.099 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[SYNPO]] | C | SSPN activity raises SYNPO's level | lines that do not express SSPN (15) vs lines expressing it (35) | 2.99× lower at baseline in the lines without SSPN | 0.023 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.9, 15.6); signed map (28.0, 3.6). **Vector** length 70.9, 14.5% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +35.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.0 | -10.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sarcospan |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:26,121,991-26,299,290 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPN1, SPN2; previously KRAG |
| Hallmark sets | PROTEIN_SECRETION, MYOGENESIS, INTERFERON_GAMMA_RESPONSE, ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14714](https://www.uniprot.org/uniprotkb/Q14714) (Sarcospan):

> Component of the dystrophin-glycoprotein complex (DGC), a complex that spans the muscle plasma membrane and forms a link between the F-actin cytoskeleton and the extracellular matrix. Preferentially associates with the sarcoglycan subcomplex of the DGC.

**Summary**, from NCBI Gene [8082](https://www.ncbi.nlm.nih.gov/gene/8082):

> This gene encodes a member of the dystrophin-glycoprotein complex (DGC). The DGC spans the sarcolemma and is comprised of dystrophin, syntrophin, alpha- and beta-dystroglycans and sarcoglycans. The DGC provides a structural link between the subsarcolemmal cytoskeleton and the extracellular matrix of muscle cells. Two alternatively spliced transcript variants that encode different protein isoforms have been described. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:11322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11322) · Entrez [8082](https://www.ncbi.nlm.nih.gov/gene/8082) · UniProt [Q14714](https://www.uniprot.org/uniprotkb/Q14714) · Ensembl [ENSG00000123096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123096)

## Data

Gene col 4400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4400); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4400]; `tensor/DDL_lfc|DDL_z.npy` [4400]; `embed/gene_vectors.npy` [4400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4400 or target_col == 4400). Every well: [[SSPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
