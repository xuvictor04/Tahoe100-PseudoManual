---
symbol: "AADACL2-AS1"
type: "gene"
col: 14335
ensembl_id: "ENSG00000242908"
name: "AADACL2 antisense RNA 1"
location: "3q25.1"
module: 21
arm: "+"
pooled_cpm: 10.76
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# AADACL2-AS1

*AADACL2 antisense RNA 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +12.5, q 3e-33, up in 32 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +11.8, q 7e-30, up in 32 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.0589×, RPMI-7951 0.0658×; ⚠ transcription drop); [[Bisoprolol (hemifumarate) (drug)]] 5 µM in 1 line (NCI-H2347 0.0419×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW 900 0.0733×); [[Finasteride (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0597×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf40]] (+0.73, fdr 7e-06), [[PRKCA-AS1]] (+0.70, fdr 1e-05), [[SPTBN1-AS2]] (+0.70, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AADAC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +12.5 | 3e-33 | 32/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +11.8 | 7e-30 | 32/43 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.4 | 6e-28 | 16/20 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.9 | 5e-13 | 22/27 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.8 | 6e-07 | 22/41 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +5.1 | 3e-05 | 21/47 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.003 | 17/43 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.1 | 0.003 | 18/45 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.031 | 15/43 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.034 | 14/46 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.040 | 6/44 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.24×** | +3.3 | 0.052 | 12/44 (LOX-IMVI, HEC-1-A, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14335.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.0589×, RPMI-7951 0.0658×; ⚠ transcription drop); [[Bisoprolol (hemifumarate) (drug)]] 5 µM in 1 line (NCI-H2347 0.0419×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW 900 0.0733×); [[Finasteride (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0597×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -4.3 | 0.010 | 13/48 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.704× | -3.4 | 0.21 | 13/47 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 8.24 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0658× (z -10.2) ⚠ transcription drop · without an alert: [[Allantoin (drug)]] 0.5 µM 0.0859× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 7.67 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0589× (z -10.8) ⚠ transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0909× (z -9.2) |
| [[A-427 (line)]] | wt | 5.59 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.100× (z -8.8) |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0957× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 7.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 1 | — | [[Finasteride (drug)]] 0.5 µM 0.0597× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.119× (z -8.8) |
| [[J82 (line)]] | alt | 7.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -9.6) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 6.12 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0419× (z -14.2) |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0733× (z -11.0) |
| [[SW480 (line)]] | alt | 7.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf40]] | +0.73 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PRKCA-AS1]] | +0.70 | +0.55 / +0.69 | both halves | 1e-05 | same gene group |
| [[SPTBN1-AS2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 | same gene group |
| [[EHBP1-AS1]] | +0.69 | +0.58 / +0.64 | both halves | 8e-06 | same gene group |
| [[MYH11]] | +0.68 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[P4HA3]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.68 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[A2ML1-AS1]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 | same gene group |
| [[SPAG5-AS1]] | +0.67 | +0.41 / +0.68 | both halves | 4e-05 | same gene group |
| [[ST7-AS2]] | +0.67 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[HRG-AS1]] | +0.67 | +0.46 / +0.62 | both halves | 2e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AADAC]] | B | AADAC activity raises AADACL2-AS1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without AADAC | 7e-04 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[AADACP1]] | B | AADACP1 activity raises AADACL2-AS1's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without AADACP1 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[IGFBP1]] | B | IGFBP1 activity raises AADACL2-AS1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.60× lower at baseline in the lines without IGFBP1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[CA2]] | B | CA2 activity raises AADACL2-AS1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without CA2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[TOP2A]] | B | TOP2A activity lowers AADACL2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CRTAC1]] | B | CRTAC1 activity raises AADACL2-AS1's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 1.33× lower at baseline in the lines without CRTAC1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.2, 27.6); signed map (32.9, 7.1). **Vector** length 67.0, 10.2% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | AADACL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.1 — chr3:151,751,443-151,928,175 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50301) · Entrez [101928142](https://www.ncbi.nlm.nih.gov/gene/101928142) · Ensembl [ENSG00000242908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242908)

## Data

Gene col 14335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14335); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14335]; `tensor/DDL_lfc|DDL_z.npy` [14335]; `embed/gene_vectors.npy` [14335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14335 or target_col == 14335). Every well: [[AADACL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AADACL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
