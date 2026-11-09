---
symbol: "EXOSC2"
type: "gene"
col: 5103
ensembl_id: "ENSG00000130713"
name: "exosome component 2"
location: "9q34.12"
module: 1
arm: "+"
pooled_cpm: 16.29
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EXOSC2

*exosome component 2* — 9q34.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.98× (z +8.9, q 3e-16, up in 34 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.78× (z +7.8, q 9e-13, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.825× (z -3.8, q 0.085, down in 15 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.216×, MIA PaCa-2 0.236×, A498 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (AsPC-1 0.0824×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.79, fdr 7e-06), [[PFAS]] (+0.79, fdr 7e-06), [[BYSL]] (+0.79, fdr 7e-06); moves opposite to [[SELENOK]] (-0.64, fdr 1e-05), [[GNAS]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +8.9 | 3e-16 | 34/44 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.90×** | +8.7 | 9e-16 | 27/41 (A-427, Hs 766T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.89×** | +8.6 | 1e-15 | 33/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +7.8 | 9e-13 | 34/47 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +7.2 | 9e-11 | 32/47 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.64×** | +6.7 | 2e-09 | 28/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.67×** | +6.7 | 2e-09 | 17/23 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +6.4 | 2e-08 | 25/46 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.9 | 2e-07 | 25/47 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.60×** | +5.9 | 2e-07 | 17/32 (SW1417, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.53×** | +5.7 | 5e-07 | 26/47 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +5.6 | 8e-07 | 24/46 (BT-474, SW480, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.51×** | +5.6 | 1e-06 | 24/47 (J82, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +5.4 | 3e-06 | 23/44 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +5.3 | 5e-06 | 25/47 (NCI-H1792, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.2 | 7e-06 | 24/48 (RKO, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 9e-05 | 21/46 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +4.4 | 4e-04 | 19/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 13/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.20× | +3.4 | 0.017 | 11/48 (A-427, HEC-1-A, …) | rises with dose | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.017 | 12/45 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.025 | 6/45 (A549, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.030 | 17/47 (BT-474, NCI-H460, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.055 | 11/45 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5103.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.216×, MIA PaCa-2 0.236×, A498 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (AsPC-1 0.0824×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.825×** | -3.8 | 0.085 | 15/48 (RKO, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.5 | 0.13 | 20/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.797× | -3.1 | 0.25 | 11/48 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.25 | 19/47 (A-427, SK-MEL-2, …) | top dose only | composition shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.735× | -3.0 | 0.27 | 8/48 (A498, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.22 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0824× (z -8.9) |
| [[C-33 A (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[PFAS]] | +0.79 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[BYSL]] | +0.79 | +0.81 / +0.79 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 816 |
| [[MYBBP1A]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[URB2]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[TBRG4]] | +0.74 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[FARSB]] | +0.73 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[MAK16]] | +0.73 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[GNAS]] | -0.64 | -0.59 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises EXOSC2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without TERT | 0.016 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.8, -37.8); signed map (-4.9, -46.2). **Vector** length 93.3, 20.4% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 15); *MYC targets v2* (hallmark, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.5 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.12 — chr9:130,693,721-130,707,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRrp4p, Rrp4p, RRP4, p7 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13868](https://www.uniprot.org/uniprotkb/Q13868) (Exosome complex component RRP4):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [23404](https://www.ncbi.nlm.nih.gov/gene/23404):

> Predicted to enable RNA binding activity. Involved in RNA catabolic process; RNA processing; and positive regulation of cell growth. Located in cytosol; nucleolus; and nucleoplasm. Part of nuclear exosome (RNase complex). Implicated in short stature, hearing loss, retinitis pigmentosa, and distinctive facies. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17097) · Entrez [23404](https://www.ncbi.nlm.nih.gov/gene/23404) · UniProt [Q13868](https://www.uniprot.org/uniprotkb/Q13868) · Ensembl [ENSG00000130713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130713)

## Data

Gene col 5103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5103); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5103]; `tensor/DDL_lfc|DDL_z.npy` [5103]; `embed/gene_vectors.npy` [5103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5103 or target_col == 5103). Every well: [[EXOSC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
