---
symbol: "PCNX4-DT"
type: "gene"
col: 15113
ensembl_id: "ENSG00000258553"
name: "PCNX4 divergent transcript"
location: "14q23.1"
module: 10
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PCNX4-DT

*PCNX4 divergent transcript* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.68× (z +23.2, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.559× (z -4.7, q 0.002, down in 18 of 45 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.613× (z -3.7, q 0.027, down in 13 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.90, fdr 7e-06), [[MAD2L1-DT]] (+0.88, fdr 8e-06), [[PKN2-AS1]] (+0.88, fdr 8e-06); moves opposite to [[FAM118A]] (-0.77, fdr 1e-05), [[MAST3]] (-0.74, fdr 1e-04), [[L2HGDH]] (-0.74, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC00882]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.68×** | +23.2 | 0e+00 | 38/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.64×** | +17.5 | 0e+00 | 38/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.00×** | +14.4 | 7e-45 | 35/37 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.53×** | +9.8 | 2e-20 | 21/33 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.9 | 3e-13 | 23/47 (AN3 CA, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.37×** | +6.9 | 4e-10 | 26/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +6.9 | 4e-10 | 24/45 (NCI-H1573, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.27×** | +6.6 | 3e-09 | 24/45 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +6.6 | 3e-09 | 22/38 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +5.6 | 1e-06 | 22/42 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +5.6 | 1e-06 | 22/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +5.4 | 3e-06 | 16/42 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.2 | 7e-06 | 3/6 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.0 | 2e-05 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.86×** | +4.8 | 6e-05 | 16/42 (NCI-H23, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.75×** | +4.3 | 5e-04 | 17/40 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.70×** | +4.3 | 7e-04 | 20/44 (SK-MEL-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.559×** | -4.7 | 0.002 | 18/45 (SW480, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.595×** | -4.2 | 0.008 | 13/47 (H4, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.625×** | -3.8 | 0.027 | 12/32 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -3.7 | 0.027 | 13/43 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.641×** | -3.6 | 0.037 | 13/46 (AN3 CA, J82, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.067 | 12/44 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.661×** | -3.3 | 0.067 | 15/45 (AsPC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -3.3 | 0.080 | 12/44 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.671×** | -3.2 | 0.080 | 15/44 (HOP62, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.64 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.94× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 2.48 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +10.0) | [[Decitabine (drug)]] 0.05 µM 0.0720× (z -8.6) |
| [[LoVo (line)]] | wt | 2.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 5.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 3.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +16.2) | — |
| [[A-172 (line)]] | wt | 3.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 8.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 4.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +11.8) | — |
| [[KATO III (line)]] | alt | 2.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 5.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.4× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 7.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +13.5) | — |
| [[SW48 (line)]] | wt | 8.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +8.5) | — |
| [[A-427 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.90 | +0.91 / +0.67 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.88 | +0.90 / +0.58 | both halves | 8e-06 | same gene group |
| [[PKN2-AS1]] | +0.88 | +0.89 / +0.58 | both halves | 8e-06 |  |
| [[LINC00240]] | +0.84 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.84 | +0.84 / +0.45 | both halves | 3e-05 | same gene group |
| [[DPH6-DT]] | +0.83 | +0.84 / +0.63 | both halves | 7e-06 | same gene group |
| [[NEB]] | +0.83 | +0.88 / +0.51 | both halves | 1e-05 |  |
| [[INO80D]] | +0.83 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.83 | +0.84 / +0.42 | both halves | 4e-05 |  |
| [[SEPTIN7-DT]] | +0.82 | +0.85 / +0.48 | both halves | 2e-05 | same gene group |
| [[ERCC6L2-AS1]] | +0.82 | +0.84 / +0.41 | both halves | 4e-05 |  |
| [[PATL2]] | +0.82 | +0.86 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.77 | -0.73 / -0.52 | both halves | 1e-05 |  |
| [[MAST3]] | -0.74 | -0.68 / -0.33 | both halves | 1e-04 |  |
| [[L2HGDH]] | -0.74 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.72 | -0.72 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00882]] | B | LINC00882 activity raises PCNX4-DT's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without LINC00882 | 0.012 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC |
| [[LINC02977]] | B | LINC02977 activity lowers PCNX4-DT's level | lines that do not express LINC02977 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without LINC02977 | 0.021 | ⚠ within organs, on part of the lines; also absent: SUSD1, FAM83G; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PCNX4-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KIF21B]] | B | KIF21B activity lowers PCNX4-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without KIF21B | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NNT-AS1]] | B | NNT-AS1 activity lowers PCNX4-DT's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without NNT-AS1 | 0.059 | ⚠ within organs, on part of the lines; co-absent genes |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises PCNX4-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SUCLG2-DT | 0.069 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[ST8SIA5]] | B | ST8SIA5 activity raises PCNX4-DT's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without ST8SIA5 | 0.085 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PCNX4-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PCNX4-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02516]] | B | LINC02516 activity raises PCNX4-DT's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 1.37× lower at baseline in the lines without LINC02516 | 0.097 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises PCNX4-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without FSIP2-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[FAP]] | B | FAP activity raises PCNX4-DT's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without FAP | 0.097 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.897). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 14.8); signed map (27.3, -10.0). **Vector** length 87.9, 17.4% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +23.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +17.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.1 | -4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.4 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PCNX4 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q23.1 — chr14:59,969,116-60,091,783 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55447) · Entrez [105370524](https://www.ncbi.nlm.nih.gov/gene/105370524) · Ensembl [ENSG00000258553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258553)

## Data

Gene col 15113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15113); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15113]; `tensor/DDL_lfc|DDL_z.npy` [15113]; `embed/gene_vectors.npy` [15113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15113 or target_col == 15113). Every well: [[PCNX4-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNX4-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
