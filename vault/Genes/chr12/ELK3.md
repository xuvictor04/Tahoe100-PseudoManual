---
symbol: "ELK3"
type: "gene"
col: 3196
ensembl_id: "ENSG00000111145"
name: "ETS transcription factor ELK3"
location: "12q23.1"
module: 147
arm: "+"
pooled_cpm: 115.12
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 53
n_dd_up_clean: 10
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 17
direction_downstream: 9
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# ELK3

*ETS transcription factor ELK3* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Peretinoin (drug)]] 5 µM: 1.65× (z +8.2, q 2e-13, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.303× (z -28.5, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGA2]] (+0.76, fdr 7e-06), [[BCAR3]] (+0.76, fdr 7e-06), [[PXN]] (+0.75, fdr 7e-06); moves opposite to [[MAP3K2]] (-0.56, fdr 8e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[ITGB1-DT]] → it (grade B ⚠); 9 go from it, the strongest it → [[RASA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **1.65×** | +8.2 | 2e-13 | 33/43 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.60×** | +8.0 | 3e-13 | 31/44 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +7.9 | 6e-13 | 29/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.57×** | +7.7 | 2e-12 | 31/43 (SW 900, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.3 | 3e-11 | 27/45 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.0 | 2e-10 | 24/38 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.46×** | +6.5 | 7e-09 | 27/44 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 5e-07 | 29/44 (NCI-H2030, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 1e-05 | 24/43 (SW 900, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 23/44 (HepG2/C3A, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 9e-04 | 24/43 (A-172, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 22/44 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.002 | 18/41 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.3 | 0.035 | 10/44 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.043 | 10/45 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.89×** | +3.1 | 0.077 | 9/42 (CFPAC-1, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 13 with an alert ⚠; shown: the 15 strongest. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.303×** | -28.5 | 0e+00 | 43/44 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.286×** | -21.2 | 0e+00 | 43/44 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -16.9 | 0e+00 | 42/44 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.500×** | -16.6 | 0e+00 | 37/45 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.402×** | -15.4 | 0e+00 | 37/44 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.382×** | -15.3 | 0e+00 | 41/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.403×** | -14.8 | 0e+00 | 36/43 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.501×** | -14.4 | 3e-45 | 40/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.434×** | -14.1 | 2e-43 | 37/45 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.525×** | -13.1 | 3e-37 | 38/44 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.452×** | -12.9 | 2e-36 | 36/44 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.458×** | -12.3 | 5e-33 | 39/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -11.0 | 1e-26 | 33/44 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.514×** | -10.4 | 1e-23 | 35/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.642×** | -10.2 | 1e-22 | 35/44 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 147 | 0 | 25 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.489× (z -23.3) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 221 | 0 | 24 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.416× (z -25.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.167× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 155 | 0 | 22 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 79.7 | 0 | 22 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -22.2) |
| [[RKO (line)]] | wt | 377 | 0 | 22 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0661× (z -29.6) |
| [[AsPC-1 (line)]] | alt | 367 | 0 | 21 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0457× (z -27.7) |
| [[SW480 (line)]] | alt | 72.5 | 0 | 17 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -28.1) |
| [[J82 (line)]] | alt | 154 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 15 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.392× (z -26.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.184× (z -14.0) |
| [[SW48 (line)]] | wt | 164 | 0 | 13 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -24.2) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 11 | — | [[Trametinib (drug)]] 0.5 µM 0.211× (z -12.6) |
| [[A-172 (line)]] | wt | 146 | 2 (2 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.9) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.209× (z -15.7) |
| [[H4 (line)]] | wt | 138 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.1) |
| [[NCI-H1573 (line)]] | alt | 261 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0441× (z -32.3) |
| [[C32 (line)]] | wt | 50.5 | 0 | 8 | — | [[Binimetinib (drug)]] 0.5 µM 0.277× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 339 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -18.2) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 173 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -30.8) |
| [[A549 (line)]] | wt | 200 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0934× (z -22.5) |
| [[CFPAC-1 (line)]] | alt | 94.2 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -15.4) |
| [[SW1417 (line)]] | alt | 70.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.9) |
| [[COLO 205 (line)]] | alt | 38.9 | 1 | 4 | [[Peretinoin (drug)]] 5 µM 3.75× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -16.5) |
| [[HS-578T (line)]] | alt | 83.9 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.286× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 75.7 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.475× (z -17.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.295× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 96.9 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.522× (z -23.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 97.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.3) |
| [[A-427 (line)]] | wt | 119 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -31.0) |
| [[PANC-1 (line)]] | alt | 87.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.7) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -14.4) |
| [[LoVo (line)]] | wt | 34.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -13.7) |
| [[SW 1271 (line)]] | alt | 156 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.2) |
| [[A498 (line)]] | wt | 67.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.0) |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.7) |
| [[HCT15 (line)]] | alt | 53.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.6) |
| [[LS 180 (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.4) |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0684× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 96.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.2) |
| [[SNU-1 (line)]] | wt | 40.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.150× (z -11.5) |
| [[SNU-423 (line)]] | alt | 78.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -8.8) |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -9.9) |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.7) |
| [[BT-474 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA2]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[BCAR3]] | +0.76 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PXN]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ACTN1]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.72 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.71 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[NT5E]] | +0.69 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K2]] | -0.56 | -0.37 / -0.56 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB1-DT]] | B | ITGB1-DT activity raises ELK3's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.76× lower at baseline in the lines without ITGB1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[LTBP2]] | B | LTBP2 activity raises ELK3's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without LTBP2 | 0.014 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[LINC02454]] | B | LINC02454 activity raises ELK3's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without LINC02454 | 0.015 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity raises ELK3's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without CCND1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ELK3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLMP]] | B | CLMP activity raises ELK3's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without CLMP | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[DAW1]] | B | DAW1 activity raises ELK3's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.94× lower at baseline in the lines without DAW1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[ROBO4]] | B | ROBO4 activity raises ELK3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without ROBO4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[TMEM156]] | B | TMEM156 activity raises ELK3's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without TMEM156 | 0.063 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ITGB1-DT]] | B | ITGB1-DT activity strengthens ELK3's drug response | lines that do not express ITGB1-DT (17) vs lines expressing it (29) | the lines without ITGB1-DT respond 0.61× as strongly (z diff +2.45); strongest at Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.39x (z diff +3.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AKAP12]] | B | AKAP12 activity raises ELK3's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without AKAP12 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[BCAR3]] | B | BCAR3 activity raises ELK3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without BCAR3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA2]] | C | ELK3's natural level strengthens RASA2's drug response | ELK3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.58; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MAMLD1]] | C | ELK3 activity raises MAMLD1's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 5.92× lower at baseline in the lines without ELK3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |
| [[MAP4K4]] | C | ELK3 activity raises MAP4K4's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 3.23× lower at baseline in the lines without ELK3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; co-absent with the target; its own permutation p |
| [[GSTO1]] | C | ELK3 activity raises GSTO1's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without ELK3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |
| [[ARHGAP31]] | C | ELK3 activity raises ARHGAP31's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 6.91× lower at baseline in the lines without ELK3 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent |
| [[KIF13A]] | C | ELK3 activity raises KIF13A's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without ELK3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |
| [[SMAGP]] | C | ELK3 activity raises SMAGP's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without ELK3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |
| [[EPB41]] | C | ELK3 activity lowers EPB41's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 1.85× higher at baseline in the lines without ELK3 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent |
| [[SREBF1]] | C | ELK3's natural level weakens SREBF1's drug response | ELK3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.55; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.889). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.2, 7.3); signed map (8.1, 45.3). **Vector** length 146, 55.2% of its response variance represented; |z| ≥ 3 in 1,874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +7.6 | +8.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +7.5 | +7.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.3 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.6 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.9 | +6.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.4 | +5.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -10.9 | -14.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -10.6 | -15.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -10.1 | -14.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -9.9 | -12.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.9 | -12.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -9.7 | -14.8 |

## What is on record

|  |  |
|---|---|
| Name | ETS transcription factor ELK3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:96,194,375-96,269,824 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERP, NET, SAP2 |
| Gene groups (HGNC) | ETS transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [P41970](https://www.uniprot.org/uniprotkb/P41970) (ETS domain-containing protein Elk-3):

> May be a negative regulator of transcription, but can activate transcription when coexpressed with Ras, Src or Mos. Forms a ternary complex with the serum response factor and the ETS and SRF motifs of the Fos serum response element.

**Summary**, from NCBI Gene [2004](https://www.ncbi.nlm.nih.gov/gene/2004):

> This gene encodes a member of the ETS-domain transcription factor family and the ternary complex factor (TCF) subfamily. Proteins in this subfamily regulate transcription when recruited by serum response factor to bind to serum response elements. This protein is activated by signal-induced phosphorylation; studies in rodents suggest that it is a transcriptional inhibitor in the absence of Ras, but activates transcription when Ras is present. Alternate splicing results in multiple transcript …

**Accessions** — [HGNC:3325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3325) · Entrez [2004](https://www.ncbi.nlm.nih.gov/gene/2004) · UniProt [P41970](https://www.uniprot.org/uniprotkb/P41970) · Ensembl [ENSG00000111145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111145)

## Data

Gene col 3196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3196); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3196]; `tensor/DDL_lfc|DDL_z.npy` [3196]; `embed/gene_vectors.npy` [3196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3196 or target_col == 3196). Every well: [[ELK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
