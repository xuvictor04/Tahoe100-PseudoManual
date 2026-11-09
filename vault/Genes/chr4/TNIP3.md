---
symbol: "TNIP3"
type: "gene"
col: 569
ensembl_id: "ENSG00000050730"
name: "TNFAIP3 interacting protein 3"
location: "4q27"
module: 167
arm: "+"
pooled_cpm: 8.09
n_lines_expressing: 17
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 18
direction_downstream: 14
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# TNIP3

*TNFAIP3 interacting protein 3* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.96× (z +18.5, q 0e+00, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.631× (z -4.4, q 0.007, down in 9 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP5]] (+0.70, fdr 7e-06), [[SLFN12]] (+0.66, fdr 1e-05), [[LINC02015]] (+0.64, fdr 1e-05); moves opposite to [[CDS2]] (-0.51, fdr 2e-05), [[ABHD12]] (-0.51, fdr 3e-05), [[SDHAP4]] (-0.51, fdr 3e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SYNPO]] → it (grade B ⚠); 14 go from it, the strongest it → [[IFI44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.96×** | +18.5 | 0e+00 | 12/14 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.53×** | +13.9 | 3e-41 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.71×** | +13.4 | 7e-39 | 12/14 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.06×** | +13.4 | 2e-38 | 12/14 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +12.6 | 3e-34 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +10.5 | 1e-23 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.87×** | +9.7 | 4e-20 | 14/14 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.46×** | +8.6 | 7e-16 | 9/13 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.9 | 2e-13 | 0/13 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.9 | 3e-10 | 12/14 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.6 | 9e-07 | 4/13 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.56×** | +4.0 | 0.003 | 1/13 (SW 1088) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +4.0 | 0.003 | 2/13 (hTERT-HPNE, A498) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.004 | 6/14 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.004 | 2/13 (HS-578T, A498) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 1/13 (hTERT-HPNE) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.008 | 0/13 | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.027 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.039 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.631×** | -4.4 | 0.007 | 9/14 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.680×** | -3.7 | 0.064 | 9/14 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.064 | 5/13 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.692×** | -3.5 | 0.064 | 8/14 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.709× | -3.3 | 0.12 | 3/13 (hTERT-HPNE, H4, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.789× | -3.2 | 0.12 | 12/14 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Entrectinib (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.12 | 2/14 (BT-474, A498) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 0.711× | -3.1 | 0.13 | 6/14 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Salicylic acid (drug)]] 5 µM |  | 0.795× | -3.1 | 0.13 | 6/14 (HS-578T, RPMI-7951, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.728× | -3.0 | 0.13 | 3/13 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 0.728× | -3.0 | 0.13 | 7/13 (LOX-IMVI, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 75.0 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.0946× (z -14.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.100× (z -14.6) |
| [[A498 (line)]] | wt | 67.0 | 4 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.05× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.3) |
| [[HS-578T (line)]] | alt | 11.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +15.0) | — |
| [[CFPAC-1 (line)]] | alt | 9.07 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +11.5) | [[Tofacitinib (drug)]] 5 µM 0.116× (z -9.2) |
| [[H4 (line)]] | wt | 58.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.141× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 4.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 56.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -8.9) |
| [[BT-474 (line)]] | alt | 5.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -11.4) |
| [[A-172 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.591 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP5]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SLFN12]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[HDX]] | +0.63 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[IL7R]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[KYNU]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TCIM]] | +0.60 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[IL6]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MSC]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SERPINB7]] | +0.59 | +0.46 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDS2]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ABHD12]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PEBP1]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 3, C 15. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO]] | B | SYNPO activity raises TNIP3's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without SYNPO | 0.089 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity raises TNIP3's level | compounds that target JAK2: 2 of 3 lower it (Fedratinib, Tofacitinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[CD274]] | B | CD274 activity raises TNIP3's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.54× lower at baseline in the lines without CD274 | 0.099 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[KYNU]] | C | KYNU activity raises TNIP3's level | lines that do not express KYNU (29) vs lines expressing it (21) | 3.60× lower at baseline in the lines without KYNU | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises TNIP3's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.57× lower at baseline in the lines without PTGS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[AGTR1]] | C | AGTR1 activity raises TNIP3's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.38× lower at baseline in the lines without AGTR1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises TNIP3's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 3.11× lower at baseline in the lines without PEX5L | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[MSC]] | C | MSC activity raises TNIP3's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.11× lower at baseline in the lines without MSC | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[SERPINB7]] | C | SERPINB7 activity raises TNIP3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 3.31× lower at baseline in the lines without SERPINB7 | 0.050 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7; co-absent with the target |
| [[LINC02360]] | C | LINC02360 activity raises TNIP3's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without LINC02360 | 0.064 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1; co-absent with the target |
| [[LINC01828]] | C | LINC01828 activity raises TNIP3's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 3.14× lower at baseline in the lines without LINC01828 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent; co-absent with the target |
| [[MIR155HG]] | C | MIR155HG activity raises TNIP3's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without MIR155HG | 0.074 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | TNIP3 activity raises IFI44's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without TNIP3 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[LINC02328]] | B | TNIP3 activity raises LINC02328's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without TNIP3 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[GBP3]] | B | TNIP3 activity raises GBP3's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without TNIP3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[CASP4]] | B | TNIP3 activity raises CASP4's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without TNIP3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[STAT4]] | B | TNIP3 activity raises STAT4's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without TNIP3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[BACH1]] | B | TNIP3 activity raises BACH1's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without TNIP3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[HMGN2P46]] | B | TNIP3 activity raises HMGN2P46's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 3.56× lower at baseline in the lines without TNIP3 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[SAMD9]] | B | TNIP3 activity raises SAMD9's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.62× lower at baseline in the lines without TNIP3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[KYNU]] | C | TNIP3 activity raises KYNU's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 6.08× lower at baseline in the lines without TNIP3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[CXCL10]] | C | TNIP3 activity raises CXCL10's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without TNIP3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[SERPINB7]] | C | TNIP3 activity raises SERPINB7's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 3.57× lower at baseline in the lines without TNIP3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[IL6]] | C | TNIP3 activity raises IL6's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 6.78× lower at baseline in the lines without TNIP3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.0, 24.0); signed map (46.4, 24.5). **Vector** length 51.8, 16.3% of its response variance represented; |z| ≥ 3 in 412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | TNFAIP3 interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,131,408-121,227,466 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIND, FLJ21162, ABIN-3 |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KP6](https://www.uniprot.org/uniprotkb/Q96KP6) (TNFAIP3-interacting protein 3):

> Binds to zinc finger protein TNFAIP3 and inhibits NF-kappa-B activation induced by tumor necrosis factor, Toll-like receptor 4 (TLR4), interleukin-1 and 12-O-tetradecanoylphorbol-13-acetate. Overexpression inhibits NF-kappa-B-dependent gene expression in response to lipopolysaccharide at a level downstream of TRAF6 and upstream of IKBKB. NF-kappa-B inhibition is independent of TNFAIP3 binding.

**Summary**, from NCBI Gene [79931](https://www.ncbi.nlm.nih.gov/gene/79931):

> Enables polyubiquitin modification-dependent protein binding activity. Involved in cellular response to lipopolysaccharide; negative regulation of canonical NF-kappaB signal transduction; and pattern recognition receptor signaling pathway. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19315) · Entrez [79931](https://www.ncbi.nlm.nih.gov/gene/79931) · UniProt [Q96KP6](https://www.uniprot.org/uniprotkb/Q96KP6) · Ensembl [ENSG00000050730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050730)

## Data

Gene col 569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 569); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 569]; `tensor/DDL_lfc|DDL_z.npy` [569]; `embed/gene_vectors.npy` [569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 569 or target_col == 569). Every well: [[TNIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
