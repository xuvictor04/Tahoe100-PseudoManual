---
symbol: "PSD3"
type: "gene"
col: 7939
ensembl_id: "ENSG00000156011"
name: "pleckstrin and Sec7 domain containing 3"
location: "8p22"
module: 34
arm: "+"
pooled_cpm: 491.64
n_lines_expressing: 37
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PSD3

*pleckstrin and Sec7 domain containing 3* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +8.8, q 9e-16, up in 21 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.429× (z -23.2, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.68, fdr 7e-06), [[S100A16]] (+0.65, fdr 1e-05), [[ITPRID2]] (+0.65, fdr 9e-06); moves opposite to [[C11orf52]] (-0.65, fdr 4e-05), [[ACTR3C]] (-0.55, fdr 8e-05), [[MGC32805]] (-0.55, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CACNA2D3]] → it (grade B ⚠); 10 go from it, the strongest it → [[GPAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.8 | 9e-16 | 21/35 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 3e-06 | 19/36 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 9e-06 | 26/34 (LS 180, A-172, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.002 | 22/34 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.009 | 13/35 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.11 | 6/36 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.13 | 16/35 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.18 | 10/35 (SK-MEL-2, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.429×** | -23.2 | 0e+00 | 33/35 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -19.7 | 0e+00 | 35/36 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -14.1 | 4e-43 | 32/35 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -10.4 | 4e-23 | 32/35 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -8.6 | 6e-16 | 27/35 (A-172, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -8.2 | 3e-14 | 31/34 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -7.2 | 5e-11 | 30/35 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -6.7 | 1e-09 | 26/36 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.765×** | -5.2 | 1e-05 | 25/35 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -5.2 | 1e-05 | 23/35 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.760×** | -4.9 | 4e-05 | 18/35 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.776×** | -4.9 | 4e-05 | 25/35 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.6 | 2e-04 | 21/35 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 2e-04 | 20/35 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -4.6 | 2e-04 | 22/35 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.766×** | -4.5 | 2e-04 | 24/36 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.826×** | -4.4 | 4e-04 | 20/37 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 1,523 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -32.4) |
| [[MIA PaCa-2 (line)]] | alt | 1,942 | 0 | 19 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0440× (z -37.1) |
| [[HEC-1-A (line)]] | alt | 837 | 0 | 18 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -25.4) |
| [[NCI-H460 (line)]] | wt | 2,367 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -25.2) |
| [[SW480 (line)]] | alt | 173 | 3 | 10 | [[Tucidinostat (drug)]] 5 µM 2.15× (z +15.7) | [[Trametinib (drug)]] 0.5 µM 0.503× (z -12.5) |
| [[A-172 (line)]] | wt | 409 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.3) |
| [[CHP-212 (line)]] | wt | 677 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -29.1) |
| [[AsPC-1 (line)]] | alt | 1,354 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -17.0) |
| [[Hs 766T (line)]] | wt | 776 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -26.1) |
| [[HS-578T (line)]] | alt | 1,510 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -19.6) |
| [[KATO III (line)]] | alt | 229 | 1 | 6 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 976 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -24.3) |
| [[A549 (line)]] | wt | 524 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.7) |
| [[PANC-1 (line)]] | alt | 190 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -20.9) |
| [[NCI-H1573 (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.1) |
| [[H4 (line)]] | wt | 233 | 1 | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.07× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.3) |
| [[LS 180 (line)]] | wt | 553 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 268 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 180 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 1.73× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.468× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 216 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 1.95× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.6) |
| [[SNU-423 (line)]] | alt | 373 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.4) |
| [[SW 900 (line)]] | alt | 304 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.4) |
| [[C32 (line)]] | wt | 147 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.478× (z -12.3) |
| [[LoVo (line)]] | wt | 347 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -17.1) |
| [[HOP62 (line)]] | alt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.1) |
| [[SHP-77 (line)]] | alt | 657 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -17.1) |
| [[SW 1088 (line)]] | alt | 863 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.3) |
| [[SW48 (line)]] | wt | 125 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.0) |
| [[A-427 (line)]] | wt | 140 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.654× (z -9.0) |
| [[A498 (line)]] | wt | 337 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 216 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -8.5) |
| [[AN3 CA (line)]] | alt | 83.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 121 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 47.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 112 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 55.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 115 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 514 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 47.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 61.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 77.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 89.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[S100A16]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ITPRID2]] | +0.65 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[SH3BGRL3]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FLNB]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ITGA2]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TMC7]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DGKD]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 | same gene group |
| [[TINAGL1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TIAM1]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 | same gene group |
| [[PAQR5]] | +0.59 | +0.61 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf52]] | -0.65 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[ACTR3C]] | -0.55 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[MGC32805]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[HOTAIR]] | -0.55 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[FAM111A-DT]] | -0.53 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[VPS33A]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ARFGEF2]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[MAIP1]] | -0.51 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[C1orf43]] | -0.51 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[SAFB]] | -0.50 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.50 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TRPM7]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D3]] | B | CACNA2D3 activity raises PSD3's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without CACNA2D3 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PSD3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PMEPA1]] | B | PMEPA1 activity raises PSD3's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without PMEPA1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[FERMT1]] | B | FERMT1 activity raises PSD3's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without FERMT1 | 0.095 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPAT3]] | B | PSD3 activity raises GPAT3's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.82× lower at baseline in the lines without PSD3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[GRB10]] | B | PSD3 activity raises GRB10's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 3.58× lower at baseline in the lines without PSD3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[ASPH]] | B | PSD3 activity raises ASPH's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without PSD3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[FERMT1]] | B | PSD3 activity raises FERMT1's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without PSD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[PPP3CA]] | B | PSD3 activity raises PPP3CA's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without PSD3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[LAMA3]] | B | PSD3 activity raises LAMA3's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without PSD3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[LAMC2]] | B | PSD3 activity raises LAMC2's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without PSD3 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[F3]] | B | PSD3 activity raises F3's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without PSD3 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | PSD3 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PSD3 (13) vs lines expressing it (35) | the lines without PSD3: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[ITGA2]] | B | PSD3 activity raises ITGA2's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 3.10× lower at baseline in the lines without PSD3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.4, 3.9); signed map (3.9, 42.9). **Vector** length 132, 44.6% of its response variance represented; |z| ≥ 3 in 1,563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.1 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.7 | -4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.0 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.2 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.1 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin and Sec7 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:18,527,303-19,084,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0942, HCA67, EFA6R, DKFZp761K1423, EFA6D |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Pleckstrin and Sec7 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYI0](https://www.uniprot.org/uniprotkb/Q9NYI0) (PH and SEC7 domain-containing protein 3):

> Guanine nucleotide exchange factor for ARF6.

**Summary**, from NCBI Gene [23362](https://www.ncbi.nlm.nih.gov/gene/23362):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in vesicle-mediated transport. Predicted to be located in membrane. Predicted to be active in glutamatergic synapse; postsynapse; and ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19093) · Entrez [23362](https://www.ncbi.nlm.nih.gov/gene/23362) · UniProt [Q9NYI0](https://www.uniprot.org/uniprotkb/Q9NYI0) · Ensembl [ENSG00000156011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156011)

## Data

Gene col 7939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7939); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7939]; `tensor/DDL_lfc|DDL_z.npy` [7939]; `embed/gene_vectors.npy` [7939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7939 or target_col == 7939). Every well: [[PSD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
