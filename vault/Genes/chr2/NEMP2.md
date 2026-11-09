---
symbol: "NEMP2"
type: "gene"
col: 12119
ensembl_id: "ENSG00000189362"
name: "nuclear envelope integral membrane protein 2"
location: "2q32.2"
module: 116
arm: "+"
pooled_cpm: 15.16
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# NEMP2

*nuclear envelope integral membrane protein 2* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.38× (z +11.5, q 5e-28, up in 8 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Demeclocycline (drug)]] 5 µM: 1.25× (z +4.4, q 0.002, up in 17 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.460× (z -10.7, q 7e-24, down in 27 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUV39H2]] (+0.59, fdr 1e-05), [[NUP188]] (+0.58, fdr 1e-05), [[LINC00941]] (+0.57, fdr 1e-05); moves opposite to [[TOM1]] (-0.61, fdr 1e-05), [[SAT2]] (-0.58, fdr 1e-05), [[BLVRB]] (-0.56, fdr 2e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ESM1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NRK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +11.5 | 5e-28 | 8/15 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.6 | 2e-19 | 17/26 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.2 | 9e-08 | 7/18 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +4.4 | 0.002 | 17/40 (SW480, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.015 | 6/38 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.063 | 3/15 (CFPAC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.063 | 4/40 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.18× | +3.3 | 0.075 | 3/41 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.460×** | -10.7 | 7e-24 | 27/39 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.478×** | -10.2 | 9e-22 | 26/40 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -9.9 | 1e-20 | 25/40 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.528×** | -8.8 | 2e-16 | 26/40 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -6.6 | 6e-09 | 20/36 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -6.5 | 1e-08 | 19/38 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.667×** | -5.6 | 2e-06 | 16/36 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.701×** | -4.7 | 2e-04 | 13/39 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.717×** | -4.3 | 1e-03 | 18/37 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -4.0 | 0.003 | 12/40 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -4.0 | 0.004 | 12/40 (NCI-H460, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.636×** | -3.2 | 0.055 | 13/38 (RKO, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.085 | 10/40 (RKO, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.088 | 7/40 (LoVo, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 179 | 0 | 28 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0567× (z -31.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.119× (z -23.6) |
| [[NCI-H460 (line)]] | wt | 36.7 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0854× (z -12.0) |
| [[Hs 766T (line)]] | wt | 47.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0524× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 94.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.471× (z -16.7) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 5 µM 0.157× (z -11.0) |
| [[LoVo (line)]] | wt | 11.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0966× (z -12.8) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.0) |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.05 µM 0.0605× (z -9.0) |
| [[J82 (line)]] | alt | 8.03 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 7.07 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0874× (z -11.4) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.8) |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUV39H2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[NUP188]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CASC19]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[LINC02742]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ESM1]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PDCD1LG2]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[XRCC2]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ADAT1]] | +0.53 | +0.36 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SAT2]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ALKBH7]] | -0.55 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[TBC1D17]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[VPS37D]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FBXW5]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[LAMTOR4]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[COX14]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MKNK2]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PCGF1]] ⚠ | -0.51 | -0.47 / -0.50 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KBTBD3]] | -0.51 | -0.37 / -0.55 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESM1]] | B | ESM1 activity raises NEMP2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.87× lower at baseline in the lines without ESM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[RGS4]] | B | RGS4 activity raises NEMP2's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without RGS4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[CCDC190]] | B | CCDC190 activity raises NEMP2's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.76× lower at baseline in the lines without CCDC190 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises NEMP2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without PDCD1LG2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRK]] | B | NEMP2 activity lowers NRK's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 2.38× higher at baseline in the lines without NEMP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[CPSF3]] | B | NEMP2 activity raises CPSF3's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without NEMP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[BRI3]] | B | NEMP2 activity lowers BRI3's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without NEMP2 | 0.066 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[ZNF121]] | B | NEMP2 activity raises ZNF121's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.18× lower at baseline in the lines without NEMP2 | 0.078 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[LAMTOR4]] | B | NEMP2 activity lowers LAMTOR4's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without NEMP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-36.5, -35.5); signed map (12.2, 45.1). **Vector** length 80.5, 15.8% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | -0.1 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.7 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -9.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear envelope integral membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,504,338-190,534,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM194B |
| Matched by | ensembl_id |

UniProt [A6NFY4](https://www.uniprot.org/uniprotkb/A6NFY4) carries no function annotation.

**Summary**, from NCBI Gene [100131211](https://www.ncbi.nlm.nih.gov/gene/100131211):

> Predicted to be located in nuclear inner membrane. Predicted to be active in nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33700) · Entrez [100131211](https://www.ncbi.nlm.nih.gov/gene/100131211) · UniProt [A6NFY4](https://www.uniprot.org/uniprotkb/A6NFY4) · Ensembl [ENSG00000189362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189362)

## Data

Gene col 12119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12119); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12119]; `tensor/DDL_lfc|DDL_z.npy` [12119]; `embed/gene_vectors.npy` [12119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12119 or target_col == 12119). Every well: [[NEMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
