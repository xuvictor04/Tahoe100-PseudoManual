---
symbol: "CNTNAP4"
type: "gene"
col: 7665
ensembl_id: "ENSG00000152910"
name: "contactin associated protein family member 4"
location: "16q23.1"
module: 90
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CNTNAP4

*contactin associated protein family member 4* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.78× (z +15.9, q 0e+00, up in 21 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0670×; ⚠ cell-cycle shift, explains ~10% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.0746×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0782×; ⚠ cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.280×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN5]] (+0.82, fdr 7e-06), [[CNTNAP5]] (+0.81, fdr 7e-06), [[LINC02208]] (+0.80, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01320]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.78×** | +15.9 | 0e+00 | 21/24 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.00×** | +15.8 | 0e+00 | 1/2 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.33×** | +15.6 | 0e+00 | 6/8 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.61×** | +15.3 | 0e+00 | 19/26 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.12×** | +11.0 | 3e-26 | 1/2 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +5.7 | 9e-07 | 6/26 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.4 | 5e-06 | 9/22 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.24×** | +5.2 | 1e-05 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.0 | 3e-05 | 3/14 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +4.8 | 8e-05 | 9/44 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +4.8 | 8e-05 | 11/39 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.6 | 2e-04 | 2/10 (NCI-H460, PANC-1) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.4 | 5e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +4.3 | 9e-04 | 11/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 8/31 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 4/15 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.007 | 10/41 (SW480, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +3.7 | 0.007 | 2/33 (SK-MEL-2, NCI-H1573) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.022 | 0/10 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.040 | 2/42 (H4, SW1417) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.069 | 0/30 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +2.9 | 0.074 | 2/29 (SK-MEL-2, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0670×; ⚠ cell-cycle shift, explains ~10% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.0746×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0782×; ⚠ cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.280×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.652× | -3.3 | 0.34 | 1/41 (hTERT-HPNE) | inconsistent across doses |  |
| [[Perindopril (erbumine) (drug)]] 0.5 µM |  | 0.681× | -3.2 | 0.34 | 7/43 (SNU-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 79.8 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0670× (z -16.4) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.9) |
| [[A-172 (line)]] | wt | 1.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.8× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 2.46 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.100× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 7.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +13.3) | — |
| [[SW480 (line)]] | alt | 1.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.8) | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.902 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.922 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.911 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN5]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 | STRING 964 |
| [[CNTNAP5]] | +0.81 | +0.70 / +0.83 | both halves | 7e-06 | same gene group |
| [[LINC02208]] | +0.80 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[AGBL1]] | +0.77 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[USH2A]] | +0.77 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.76 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[GLRA3]] | +0.76 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.76 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises CNTNAP4's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.17× lower at baseline in the lines without LINC01320 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[LINC01287]] | B | LINC01287 activity raises CNTNAP4's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without LINC01287 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[TOP2A]] | B | TOP2A activity lowers CNTNAP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BAALC]] | B | BAALC activity raises CNTNAP4's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.79× lower at baseline in the lines without BAALC | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | CNTNAP4's natural level weakens CLVS1's drug response | CNTNAP4's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.43; direction clear | 0.038 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.9, 28.9); signed map (33.6, 14.7). **Vector** length 41.0, 5.00% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:76,277,278-76,560,757 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CASPR4, KIAA1763 |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0A0](https://www.uniprot.org/uniprotkb/Q9C0A0) (Contactin-associated protein-like 4):

> Presynaptic protein involved in both dopaminergic synaptic transmission and GABAergic system, thereby participating in the structural maturation of inhibitory interneuron synapses. Involved in the dopaminergic synaptic transmission by attenuating dopamine release through a presynaptic mechanism. Also participates in the GABAergic system (By similarity).

**Summary**, from NCBI Gene [85445](https://www.ncbi.nlm.nih.gov/gene/85445):

> This gene encodes a member of the neurexin protein family. Members of this family function in the vertebrate nervous system as cell adhesion molecules and receptors. This protein contains epidermal growth factor repeats and laminin G domains. In addition, it includes an F5/8 type C domain, discoidin/neuropilin- and fibrinogen-like domains, and thrombospondin N-terminal-like domains. This protein may also play a role in proper neurotransmission in the dopaminergic and GABAergic systems and …

**Accessions** — [HGNC:18747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18747) · Entrez [85445](https://www.ncbi.nlm.nih.gov/gene/85445) · UniProt [Q9C0A0](https://www.uniprot.org/uniprotkb/Q9C0A0) · Ensembl [ENSG00000152910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152910)

## Data

Gene col 7665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7665); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7665]; `tensor/DDL_lfc|DDL_z.npy` [7665]; `embed/gene_vectors.npy` [7665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7665 or target_col == 7665). Every well: [[CNTNAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
