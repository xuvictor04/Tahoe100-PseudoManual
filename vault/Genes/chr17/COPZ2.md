---
symbol: "COPZ2"
type: "gene"
col: 76
ensembl_id: "ENSG00000005243"
name: "coat protein complex I subunit zeta 2"
location: "17q21.32"
module: 15
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 42
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# COPZ2

*coat protein complex I subunit zeta 2* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.35× (z +21.6, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -7.6, q 2e-11, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALINC1]] (+0.69, fdr 1e-05), [[PJVK]] (+0.68, fdr 1e-05), [[CNPY2-AS1]] (+0.68, fdr 2e-05); moves opposite to [[RRP1B]] (-0.63, fdr 4e-05), [[NAA40]] (-0.58, fdr 5e-05), [[TAF1B]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[BBOF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 76.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.35×** | +21.6 | 0e+00 | 26/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +12.3 | 3e-32 | 4/4 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.6 | 1e-28 | 9/13 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +8.8 | 2e-16 | 4/4 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.3 | 3e-08 | 10/24 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 9e-04 | 5/38 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +4.4 | 9e-04 | 4/36 (NCI-H2030, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.4 | 9e-04 | 6/27 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 6/34 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.014 | 3/25 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.6 | 0.015 | 1/14 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.036 | 2/18 (hTERT-HPNE, RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.061 | 3/37 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.2 | 0.066 | 6/26 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Flutamide (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.086 | 0/32 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 76.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -7.6 | 2e-11 | 20/36 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -6.0 | 6e-07 | 16/34 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.581×** | -5.0 | 1e-04 | 15/37 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.592×** | -4.8 | 2e-04 | 11/34 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -3.9 | 0.009 | 12/30 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.652×** | -3.9 | 0.009 | 11/37 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.658×** | -3.6 | 0.028 | 8/31 (Hs 766T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.681×** | -3.5 | 0.033 | 10/36 (HS-578T, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.713× | -3.1 | 0.13 | 11/36 (A498, H4, …) | top dose only | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 76. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.7) |
| [[A549 (line)]] | wt | 1.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0428× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 7.39 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0872× (z -8.9) |
| [[SW480 (line)]] | alt | 2.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.5) | — |
| [[A-172 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.813 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.673 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.961 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 76), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALINC1]] | +0.69 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PJVK]] | +0.68 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.68 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[C2CD5-AS1]] | +0.67 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[CATSPER2P1-1]] | +0.67 | +0.40 / +0.76 | both halves | 5e-05 |  |
| [[ST7-AS2]] | +0.67 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CDNF]] | +0.67 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[INTS6-AS1]] | +0.67 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MROH8]] | +0.67 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.66 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SPATA1]] | +0.66 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ANKHD1-DT]] | +0.66 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.63 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NAA40]] | -0.58 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TAF1B]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COPZ2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRC17]] | B | LRRC17 activity raises COPZ2's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without LRRC17 | 0.051 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises COPZ2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BBOF1]] | B | COPZ2 activity raises BBOF1's level | lines that do not express COPZ2 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without COPZ2 | 0.019 | ⚠ within organs, on part of the lines; also absent: WDR54, ADGRE5, L3MBTL1; maybe low, not absent |
| [[LINC02256]] | B | COPZ2 activity raises LINC02256's level | lines that do not express COPZ2 (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without COPZ2 | 0.067 | ⚠ within organs, on part of the lines; also absent: WDR54, ADGRE5, L3MBTL1; maybe low, not absent |
| [[GOLGA8N]] | B | COPZ2 activity raises GOLGA8N's level | lines that do not express COPZ2 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without COPZ2 | 0.072 | ⚠ within organs, on part of the lines; also absent: WDR54, ADGRE5, L3MBTL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.8, 23.9); signed map (33.7, -4.4). **Vector** length 45.7, 6.46% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +21.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.3 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.6 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | +0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit zeta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,026,167-48,038,030 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23008 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Coat protein complex I |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P299](https://www.uniprot.org/uniprotkb/Q9P299) (Coatomer subunit zeta-2):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. The zeta subunit may be involved in regulating the coat assembly and, hence, the rate of …

**Summary**, from NCBI Gene [51226](https://www.ncbi.nlm.nih.gov/gene/51226):

> This gene encodes a member of the adaptor complexes small subunit family. The encoded protein is a subunit of the coatomer protein complex, a seven-subunit complex that functions in the formation of COPI-type, non-clathrin-coated vesicles. COPI vesicles function in the retrograde Golgi-to-ER transport of dilysine-tagged proteins. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:19356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19356) · Entrez [51226](https://www.ncbi.nlm.nih.gov/gene/51226) · UniProt [Q9P299](https://www.uniprot.org/uniprotkb/Q9P299) · Ensembl [ENSG00000005243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005243)

## Data

Gene col 76: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 76); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 76, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 76]; `tensor/DDL_lfc|DDL_z.npy` [76]; `embed/gene_vectors.npy` [76]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 76 or target_col == 76). Every well: [[COPZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
