---
symbol: "GOLGA8N"
type: "gene"
col: 13857
ensembl_id: "ENSG00000232653"
name: "golgin A8 family member N"
location: "15q13.3"
module: 15
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GOLGA8N

*golgin A8 family member N* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.85× (z +6.8, q 8e-09, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +5.0, q 1e-04, up in 12 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.275× (z -8.7, q 3e-15, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02256]] (+0.86, fdr 7e-06, ⚠ same locus), [[TRIM7-AS2]] (+0.64, fdr 1e-05), [[ZFAND2A-DT]] (+0.60, fdr 1e-05), [[MDP1]] (+0.60, fdr 1e-05); moves opposite to [[VMA21]] (-0.61, fdr 1e-05), [[TFDP1]] (-0.57, fdr 1e-05), [[MTAP]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C1R]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC02256]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +6.8 | 8e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.0 | 1e-04 | 12/25 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +4.9 | 2e-04 | 4/12 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.8 | 0.017 | 4/24 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.6 | 0.040 | 6/27 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +3.5 | 0.044 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.63× | +3.1 | 0.13 | 5/31 (A498, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.59× | +3.0 | 0.17 | 6/20 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.37× | +3.0 | 0.17 | 2/37 (NCI-H2030, CFPAC-1) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.275×** | -8.7 | 3e-15 | 27/33 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.342×** | -7.2 | 2e-10 | 26/38 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.480×** | -4.9 | 2e-04 | 20/31 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -3.8 | 0.018 | 16/30 (A549, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -3.7 | 0.024 | 14/19 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.579×** | -3.7 | 0.024 | 12/39 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.587×** | -3.6 | 0.029 | 10/38 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.578×** | -3.5 | 0.034 | 11/31 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.373×** | -3.5 | 0.034 | 12/20 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -3.2 | 0.083 | 18/37 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0486× (z -11.3) |
| [[A-172 (line)]] | wt | 5.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -9.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[H4 (line)]] | wt | 6.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0432× (z -9.3) |
| [[HOP62 (line)]] | alt | 4.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0360× (z -10.9) |
| [[SNU-423 (line)]] | alt | 4.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0663× (z -9.0) |
| [[A-427 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.711 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.888 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.532 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.715 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.562 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02256]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | ⚠ same locus (5.8 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM7-AS2]] | +0.64 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.60 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[MDP1]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PIGP]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HOXA5]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RAB1A]] | +0.59 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[INTS4P1]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZMYM5]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[COPZ2]] | +0.59 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TERF2IP]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ARID4B]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.61 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[MTAP]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.56 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[NUP188]] | -0.55 | -0.37 / -0.64 | both halves | 9e-05 |  |
| [[EFTUD2]] | -0.55 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[EIF5A]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[LAS1L]] | -0.54 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[GNG12]] | -0.54 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PSME3]] | -0.53 | -0.39 / -0.65 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1R]] | B | C1R activity raises GOLGA8N's level | lines that do not express C1R (20) vs lines expressing it (30) | 1.63× lower at baseline in the lines without C1R | 0.034 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[A1BG]] | B | A1BG activity raises GOLGA8N's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without A1BG | 0.053 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[COPZ2]] | B | COPZ2 activity raises GOLGA8N's level | lines that do not express COPZ2 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without COPZ2 | 0.072 | ⚠ within organs, on part of the lines; also absent: WDR54, ADGRE5, L3MBTL1; maybe low, not absent |
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises GOLGA8N's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without NR2F2-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02256]] | B | GOLGA8N activity raises LINC02256's level | lines that do not express GOLGA8N (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without GOLGA8N | 0.037 | ⚠ within organs, on part of the lines; also absent: HECTD2, TBKBP1, TMEFF1; maybe low, not absent |
| [[CALML4]] | B | GOLGA8N activity lowers CALML4's level | lines that do not express GOLGA8N (5) vs lines expressing it (45) | 2.76× higher at baseline in the lines without GOLGA8N | 0.075 | ⚠ within organs, on part of the lines; also absent: HECTD2, TBKBP1, TMEFF1; maybe low, not absent |
| [[EFTUD2]] | B | GOLGA8N activity raises EFTUD2's level | lines that do not express GOLGA8N (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without GOLGA8N | 0.082 | ⚠ within organs, on part of the lines; also absent: HECTD2, TBKBP1, TMEFF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.5, 29.7); signed map (-5.8, 5.3). **Vector** length 43.4, 6.25% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -3.5 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | golgin A8 family member N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:32,593,456-32,607,310 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Golgin A6 and A8 families |
| Matched by | ensembl_id |

UniProt [F8WBI6](https://www.uniprot.org/uniprotkb/F8WBI6) carries no function annotation.

**Summary**, from NCBI Gene [643699](https://www.ncbi.nlm.nih.gov/gene/643699):

> Predicted to be involved in Golgi organization. Predicted to be located in Golgi apparatus. Predicted to be active in Golgi cis cisterna; Golgi cisterna membrane; and cis-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44405) · Entrez [643699](https://www.ncbi.nlm.nih.gov/gene/643699) · UniProt [F8WBI6](https://www.uniprot.org/uniprotkb/F8WBI6) · Ensembl [ENSG00000232653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232653)

## Data

Gene col 13857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13857); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13857]; `tensor/DDL_lfc|DDL_z.npy` [13857]; `embed/gene_vectors.npy` [13857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13857 or target_col == 13857). Every well: [[GOLGA8N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA8N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
