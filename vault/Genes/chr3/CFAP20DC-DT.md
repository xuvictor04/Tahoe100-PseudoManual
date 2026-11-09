---
symbol: "CFAP20DC-DT"
type: "gene"
col: 14350
ensembl_id: "ENSG00000243295"
name: "CFAP20DC divergent transcript"
location: "3p14.2"
module: 166
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# CFAP20DC-DT

*CFAP20DC divergent transcript* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.88× (z +26.1, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01500]] (+0.81, fdr 7e-06), [[SGCD]] (+0.78, fdr 7e-06), [[SLC14A2]] (+0.77, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC02240]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.88×** | +26.1 | 0e+00 | 23/24 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **6.31×** | +15.6 | 0e+00 | 30/33 (NCI-H460, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.60×** | +15.3 | 0e+00 | 20/29 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.80×** | +14.9 | 0e+00 | 6/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.57×** | +12.9 | 8e-36 | 33/39 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.69×** | +12.6 | 3e-34 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +10.1 | 3e-22 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.8 | 9e-10 | 11/41 (A549, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +6.4 | 1e-08 | 11/29 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +5.3 | 5e-06 | 7/28 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.9 | 6e-05 | 1/6 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.8 | 6e-05 | 10/22 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.0 | 0.003 | 1/10 (A498) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.9 | 0.004 | 2/18 (Hs 766T, SW480) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.010 | 3/36 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.010 | 4/31 (C32, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.015 | 9/42 (KATO III, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.074 | 5/30 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.079 | 4/43 (C32, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | 0.674× | -3.3 | 0.47 | 11/42 (SK-MEL-2, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 1.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.2× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 1.13 | 2 | 0 | [[Auranofin (drug)]] 5 µM 37.8× (z +10.1) | — |
| [[C32 (line)]] | wt | 17.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.8× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +10.8) | — |
| [[LoVo (line)]] | wt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 1.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +9.6) | — |
| [[SW480 (line)]] | alt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +11.8) | — |
| [[A-172 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01500]] | +0.81 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[SGCD]] | +0.78 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[SLC14A2]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[RFTN2]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.75 | +0.55 / +0.79 | both halves | 1e-05 |  |
| [[DPP6]] | +0.74 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[KCNAB1]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[LINC01358]] | +0.73 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ESR1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.72 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[DCC]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02240]] | B | LINC02240 activity raises CFAP20DC-DT's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without LINC02240 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[PDZRN3]] | B | PDZRN3 activity raises CFAP20DC-DT's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without PDZRN3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[BAALC]] | B | BAALC activity raises CFAP20DC-DT's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without BAALC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[HTR1F]] | B | HTR1F activity raises CFAP20DC-DT's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without HTR1F | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CFAP20DC-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRC17]] | B | LRRC17 activity raises CFAP20DC-DT's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without LRRC17 | 0.028 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[LINC02109]] | B | LINC02109 activity raises CFAP20DC-DT's level | lines that do not express LINC02109 (40) vs lines expressing it (10) | 2.01× lower at baseline in the lines without LINC02109 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287474, ENSG00000253642, LINC00879 |
| [[TEK]] | B | TEK activity raises CFAP20DC-DT's level | lines that do not express TEK (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without TEK | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent |
| [[KCNE4]] | B | KCNE4 activity raises CFAP20DC-DT's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without KCNE4 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[TF]] | B | TF activity raises CFAP20DC-DT's level | lines that do not express TF (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without TF | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1 |
| [[FYB1]] | B | FYB1 activity raises CFAP20DC-DT's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.65× lower at baseline in the lines without FYB1 | 0.098 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.3, 26.7); signed map (30.2, 14.8). **Vector** length 56.1, 8.76% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +26.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | CFAP20DC divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.2 — chr3:59,050,164-59,754,808 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55618) · Entrez [105377110](https://www.ncbi.nlm.nih.gov/gene/105377110) · Ensembl [ENSG00000243295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243295)

## Data

Gene col 14350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14350); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14350]; `tensor/DDL_lfc|DDL_z.npy` [14350]; `embed/gene_vectors.npy` [14350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14350 or target_col == 14350). Every well: [[CFAP20DC-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP20DC-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
