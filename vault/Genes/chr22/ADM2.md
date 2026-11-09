---
symbol: "ADM2"
type: "gene"
col: 4862
ensembl_id: "ENSG00000128165"
name: "adrenomedullin 2"
location: "22q13.33"
module: 63
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ADM2

*adrenomedullin 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 2.14× (z +9.8, q 5e-20, up in 26 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -8.3, q 6e-14, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB3]] (+0.78, fdr 7e-06), [[CHAC1]] (+0.75, fdr 7e-06), [[CEBPG]] (+0.74, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHAC1]] → it (grade B ⚠); 3 go from it, the strongest it → [[SELENOS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **2.14×** | +9.8 | 5e-20 | 26/36 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.49×** | +8.3 | 2e-14 | 28/35 (SHP-77, HS-578T, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.71×** | +6.9 | 1e-09 | 20/36 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.7 | 2e-09 | 1/7 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +6.3 | 3e-08 | 18/32 (HT-29, NCI-H2030, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.95×** | +6.1 | 1e-07 | 19/34 (SHP-77, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.83×** | +5.5 | 3e-06 | 10/27 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +5.4 | 4e-06 | 14/36 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 2e-05 | 12/35 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.1 | 2e-05 | 2/15 (HEC-1-A, A498) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +4.9 | 5e-05 | 8/36 (A498, SW 900, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +4.8 | 8e-05 | 7/24 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 7/35 (KATO III, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.2 | 9e-04 | 5/17 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 9e-04 | 10/32 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 8/31 (NCI-H460, A498, …) | top dose only |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **2.32×** | +4.0 | 0.002 | 1/21 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.76×** | +3.7 | 0.007 | 5/26 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.013 | 5/34 (LS 180, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -8.3 | 6e-14 | 23/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.461×** | -7.1 | 3e-10 | 19/33 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -6.4 | 2e-08 | 17/33 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.682×** | -5.0 | 7e-05 | 10/35 (SW480, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.354×** | -5.0 | 7e-05 | 15/27 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.4 | 0.001 | 12/28 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.3 | 0.002 | 11/31 (KATO III, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -4.1 | 0.003 | 14/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -3.6 | 0.021 | 8/37 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.482×** | -3.5 | 0.026 | 8/24 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.684×** | -3.3 | 0.049 | 11/34 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **0.715×** | -3.1 | 0.092 | 7/33 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.719× | -3.0 | 0.10 | 9/36 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.45 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0344× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0727× (z -13.1) |
| [[SW480 (line)]] | alt | 4.93 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -9.7) |
| [[KATO III (line)]] | alt | 9.92 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0256× (z -17.0) |
| [[A498 (line)]] | wt | 6.56 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 6.34 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 4.61 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0764× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 4.01 | 0 | 1 | — | [[Carbamazepine (drug)]] 5 µM 0.0618× (z -10.0) |
| [[A-172 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB3]] | +0.78 | +0.62 / +0.81 | both halves | 7e-06 | STRING 466 |
| [[CHAC1]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 | STRING 436 |
| [[CEBPG]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[CARS1]] | +0.73 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[SARS1]] | +0.72 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[SESN2]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[GARS1]] | +0.71 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[NIBAN1]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[YARS1]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.70 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[ASNS]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[AARS1]] | +0.69 | +0.57 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAC1]] | B | CHAC1 activity raises ADM2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CHAC1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOS]] | B | ADM2 activity raises SELENOS's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without ADM2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1 |
| [[MICALL1]] | B | ADM2 activity lowers MICALL1's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.63× higher at baseline in the lines without ADM2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1; its own permutation p |
| [[GFPT1]] | B | ADM2 activity raises GFPT1's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without ADM2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1 |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, 48.6); signed map (-12.3, 24.1). **Vector** length 64.5, 12.1% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.64 to 16); *mTORC1 signaling* (hallmark, mean cos +0.55 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.66 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +3.9 | +9.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +3.4 | +5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +8.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | -2.2 | -1.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | adrenomedullin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,481,543-50,486,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AM2, FLJ21135 |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Calcitonin-like ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4H4](https://www.uniprot.org/uniprotkb/Q7Z4H4) (Protein ADM2):

> Intermedin/ADM2 is a peptide hormone that plays a role as physiological regulator of gastrointestinal and cardiovascular bioactivities mediated by the CALCRL-RAMPs receptor complexes. Activates the cAMP-dependent pathway through interaction with CALCRL-RAMP3 receptor complex.

**Summary**, from NCBI Gene [79924](https://www.ncbi.nlm.nih.gov/gene/79924):

> This gene encodes a member of the calcitonin gene-related peptide (CGRP)/calcitonin family of hormones that play a role in the regulation of cardiovascular homeostasis, prolactin release, anti-diuresis, anti-natriuresis, and regulation of food and water intake. The encoded protein is proteolytically processed to generate one or more biologically active peptides. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:28898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28898) · Entrez [79924](https://www.ncbi.nlm.nih.gov/gene/79924) · UniProt [Q7Z4H4](https://www.uniprot.org/uniprotkb/Q7Z4H4) · Ensembl [ENSG00000128165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128165)

## Data

Gene col 4862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4862); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4862]; `tensor/DDL_lfc|DDL_z.npy` [4862]; `embed/gene_vectors.npy` [4862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4862 or target_col == 4862). Every well: [[ADM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
