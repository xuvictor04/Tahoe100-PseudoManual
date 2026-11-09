---
symbol: "ANPEP"
type: "gene"
col: 9365
ensembl_id: "ENSG00000166825"
name: "alanyl aminopeptidase, membrane"
location: "15q26.1"
module: 104
arm: "+"
pooled_cpm: 15.2
n_lines_expressing: 17
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# ANPEP

*alanyl aminopeptidase, membrane* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.30× (z +16.8, q 0e+00, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +9.2, q 4e-18, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.489× (z -6.9, q 3e-09, down in 15 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A1]] (+0.72, fdr 7e-06), [[COL6A3]] (+0.64, fdr 7e-06), [[CLMP]] (+0.63, fdr 7e-06); moves opposite to [[RRAD]] (-0.49, fdr 1e-04), [[PATJ]] (-0.47, fdr 2e-04), [[EXPH5]] (-0.45, fdr 7e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PATJ]] → it (grade B ⚠); 12 go from it, the strongest it → [[MAP4K4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.30×** | +16.8 | 0e+00 | 9/13 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +13.6 | 2e-39 | 9/11 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +10.7 | 2e-24 | 9/12 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +9.2 | 4e-18 | 3/15 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.4 | 0.001 | 4/15 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.004 | 7/15 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.023 | 1/15 (H4) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.044 | 4/15 (HOP62, Hs 766T, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.044 | 7/15 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.2 | 0.072 | 1/7 (H4) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -6.9 | 3e-09 | 15/15 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.665×** | -3.9 | 0.032 | 0/15 | inconsistent across doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.094 | 0/15 | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.724× | -3.2 | 0.14 | 9/15 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | 0.796× | -3.2 | 0.14 | 7/15 (SW 1271, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.800× | -3.2 | 0.15 | 4/15 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 49.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -19.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.134× (z -11.8) |
| [[PANC-1 (line)]] | alt | 65.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -23.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 91.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0394× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.133× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 76.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -16.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -12.7) |
| [[A498 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0693× (z -10.2) |
| [[HOP62 (line)]] | alt | 9.96 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -13.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.153× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0748× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.141× (z -10.0) |
| [[H4 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[Panc 03.27 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -11.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 1271 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -8.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A1]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[COL6A3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CLMP]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ITGA5]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 498 |
| [[SCUBE3]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DKK3]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[FAH]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FN1]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 448 |
| [[STEAP3]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PXDN]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 | STRING 414 |
| [[COL6A2]] | +0.56 | +0.66 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IGF2]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAD]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PATJ]] | -0.47 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[EXPH5]] | -0.45 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[GCNT2]] | -0.44 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[SSTR2]] | -0.44 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | PATJ activity lowers ANPEP's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.55× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[COL5A1]] | C | COL5A1 activity raises ANPEP's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.31× lower at baseline in the lines without COL5A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[SERPINE1]] | C | SERPINE1 activity raises ANPEP's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 4.03× lower at baseline in the lines without SERPINE1 | 0.011 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615; co-absent with the target |
| [[DCN]] | C | DCN activity raises ANPEP's level | lines that do not express DCN (39) vs lines expressing it (11) | 3.29× lower at baseline in the lines without DCN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises ANPEP's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without MMP2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises ANPEP's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 4.26× lower at baseline in the lines without DKK3 | 0.068 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises ANPEP's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without CSPG4 | 0.093 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP4K4]] | B | ANPEP activity raises MAP4K4's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without ANPEP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[MICAL2]] | B | ANPEP activity raises MICAL2's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without ANPEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[CD59]] | B | ANPEP activity raises CD59's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without ANPEP | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[PLXNA2]] | B | ANPEP activity raises PLXNA2's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without ANPEP | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[SERPINE1]] | C | ANPEP activity raises SERPINE1's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 6.58× lower at baseline in the lines without ANPEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[RFX8]] | C | ANPEP activity raises RFX8's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 4.76× lower at baseline in the lines without ANPEP | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[COL5A1]] | C | ANPEP activity raises COL5A1's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 6.74× lower at baseline in the lines without ANPEP | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[ITGA4]] | C | ANPEP activity raises ITGA4's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 3.90× lower at baseline in the lines without ANPEP | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[MMP2]] | C | ANPEP activity raises MMP2's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 5.28× lower at baseline in the lines without ANPEP | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[DKK3]] | C | ANPEP activity raises DKK3's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 5.59× lower at baseline in the lines without ANPEP | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[CLMP]] | C | ANPEP activity raises CLMP's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 5.52× lower at baseline in the lines without ANPEP | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[ITGA8]] | C | ANPEP activity raises ITGA8's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.06× lower at baseline in the lines without ANPEP | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.6, 18.7); signed map (24.1, 43.8). **Vector** length 52.3, 17.0% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +16.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | -0.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.1 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | alanyl aminopeptidase, membrane |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,784,895-89,815,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAP1, gp150, p150, AP-N, hAPN; previously CD13, PEPN |
| Gene groups (HGNC) | Aminopeptidases; CD molecules; M1 metallopeptidases |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Peptide hormone metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P15144](https://www.uniprot.org/uniprotkb/P15144) (Aminopeptidase N):

> Broad specificity aminopeptidase which plays a role in the final digestion of peptides generated from hydrolysis of proteins by gastric and pancreatic proteases. Also involved in the processing of various peptides including peptide hormones, such as angiotensin III and IV, neuropeptides, and chemokines. May also be involved the cleavage of peptides bound to major histocompatibility complex class II molecules of antigen presenting cells. May have a role in angiogenesis and promote cholesterol …

**Summary**, from NCBI Gene [290](https://www.ncbi.nlm.nih.gov/gene/290):

> Aminopeptidase N is located in the small-intestinal and renal microvillar membrane, and also in other plasma membranes. In the small intestine aminopeptidase N plays a role in the final digestion of peptides generated from hydrolysis of proteins by gastric and pancreatic proteases. Its function in proximal tubular epithelial cells and other cell types is less clear. The large extracellular carboxyterminal domain contains a pentapeptide consensus sequence characteristic of members of the …

**Accessions** — [HGNC:500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:500) · Entrez [290](https://www.ncbi.nlm.nih.gov/gene/290) · UniProt [P15144](https://www.uniprot.org/uniprotkb/P15144) · Ensembl [ENSG00000166825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166825)

## Data

Gene col 9365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9365); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9365]; `tensor/DDL_lfc|DDL_z.npy` [9365]; `embed/gene_vectors.npy` [9365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9365 or target_col == 9365). Every well: [[ANPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
