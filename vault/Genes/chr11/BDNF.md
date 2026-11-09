---
symbol: "BDNF"
type: "gene"
col: 10742
ensembl_id: "ENSG00000176697"
name: "brain derived neurotrophic factor"
location: "11p14.1"
module: 19
arm: "+"
pooled_cpm: 35.74
n_lines_expressing: 31
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# BDNF

*brain derived neurotrophic factor* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +23.9, q 0e+00, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.594× (z -7.6, q 7e-12, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAT4]] (+0.63, fdr 7e-06), [[TGFB2]] (+0.63, fdr 1e-05), [[CPED1]] (+0.59, fdr 1e-05); moves opposite to [[PCYT1A]] (-0.46, fdr 9e-05), [[TPD52L2]] (-0.44, fdr 1e-04), [[ORC3]] (-0.44, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02742]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPR176]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +23.9 | 0e+00 | 19/29 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +12.1 | 5e-31 | 17/29 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +11.9 | 1e-30 | 22/29 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.00×** | +10.6 | 7e-24 | 21/28 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 5e-14 | 14/29 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.5 | 5e-12 | 18/29 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.2 | 4e-11 | 15/29 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +5.6 | 2e-06 | 15/29 (HOP62, A498, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +5.4 | 5e-06 | 11/29 (HOP62, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 5e-06 | 15/28 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 9e-06 | 10/29 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.86×** | +5.0 | 3e-05 | 9/28 (H4, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +4.8 | 7e-05 | 14/29 (A-427, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 1e-04 | 8/29 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.5 | 3e-04 | 8/28 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 6e-04 | 11/29 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.2 | 8e-04 | 11/29 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.594×** | -7.6 | 7e-12 | 20/28 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.581×** | -7.6 | 7e-12 | 14/29 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.616×** | -7.4 | 3e-11 | 20/28 (NCI-H2030, J82, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -6.7 | 3e-09 | 19/29 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -5.6 | 2e-06 | 17/29 (NCI-H460, A-427, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.741×** | -4.4 | 0.001 | 9/29 (NCI-H460, SW 900, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.028 | 8/29 (NCI-H460, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.849× | -3.5 | 0.029 | 6/29 (Hs 766T, HT-29, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.678× | -3.1 | 0.12 | 8/28 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.12 | 4/29 (SW 1271, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.782× | -3.0 | 0.12 | 8/29 (Panc 03.27, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (drug)]] 0.5 µM |  | 0.820× | -3.0 | 0.12 | 2/29 (RPMI-7951, HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 265 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -25.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.4) |
| [[A-172 (line)]] | wt | 28.0 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.2× (z +17.7) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 192 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -10.3) |
| [[A-427 (line)]] | wt | 78.2 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.133× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.318× (z -9.3) |
| [[A498 (line)]] | wt | 11.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 13.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 3 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.221× (z -11.1) |
| [[A549 (line)]] | wt | 29.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 46.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.00× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[H4 (line)]] | wt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 9.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 9.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 32.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT4]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[TGFB2]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 | STRING 424 |
| [[CPED1]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ALPK2]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[TFAP2C]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PRICKLE1]] | +0.55 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SLFN12]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[CDH11]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GATA3]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[TPD52L2]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ORC3]] | -0.44 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[PLP2]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02742]] | B | LINC02742 activity raises BDNF's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 3.46× lower at baseline in the lines without LINC02742 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227 |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises BDNF's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.22× lower at baseline in the lines without PDCD1LG2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises BDNF's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.03× lower at baseline in the lines without FAT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises BDNF's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.22× lower at baseline in the lines without TRPC4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[COL12A1]] | C | COL12A1 activity raises BDNF's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 3.20× lower at baseline in the lines without COL12A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[SFTA1P]] | C | SFTA1P activity raises BDNF's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without SFTA1P | 0.078 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[LINC00472]] | C | LINC00472 activity raises BDNF's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 3.17× lower at baseline in the lines without LINC00472 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | C | BDNF activity raises GPR176's level | lines that do not express BDNF (19) vs lines expressing it (31) | 5.08× lower at baseline in the lines without BDNF | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA0408, IL7R, RFTN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.2, 26.2); signed map (42.9, 28.3). **Vector** length 93.5, 26.2% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +23.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.4 | -7.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.9 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | brain derived neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:27,654,893-27,722,058 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neurotrophins |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 26 pathways, smallest: Activated NTRK2 signals through PLCG1; Loss of MECP2 binding ability to 5mC-DNA; NTRK2 activates RAC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P23560](https://www.uniprot.org/uniprotkb/P23560) (Neurotrophic factor BDNF precursor form):

> Important signaling molecule that activates signaling cascades downstream of NTRK2. During development, promotes the survival and differentiation of selected neuronal populations of the peripheral and central nervous systems. Participates in axonal growth, pathfinding and in the modulation of dendritic growth and morphology. Major regulator of synaptic transmission and plasticity at adult synapses in many regions of the CNS. The versatility of BDNF is emphasized by its contribution to a range …

**Summary**, from NCBI Gene [627](https://www.ncbi.nlm.nih.gov/gene/627):

> This gene encodes a member of the nerve growth factor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protein. Binding of this protein to its cognate receptor promotes neuronal survival in the adult brain. Expression of this gene is reduced in Alzheimer's, Parkinson's, and Huntington's disease patients. This gene may play a role in the regulation of the stress …

**Accessions** — [HGNC:1033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1033) · Entrez [627](https://www.ncbi.nlm.nih.gov/gene/627) · UniProt [P23560](https://www.uniprot.org/uniprotkb/P23560) · Ensembl [ENSG00000176697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176697)

## Data

Gene col 10742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10742); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10742]; `tensor/DDL_lfc|DDL_z.npy` [10742]; `embed/gene_vectors.npy` [10742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10742 or target_col == 10742). Every well: [[BDNF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BDNF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
