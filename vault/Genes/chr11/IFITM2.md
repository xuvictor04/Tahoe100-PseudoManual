---
symbol: "IFITM2"
type: "gene"
col: 11638
ensembl_id: "ENSG00000185201"
name: "interferon induced transmembrane protein 2"
location: "11p15.5"
module: 32
arm: "+"
pooled_cpm: 34.44
n_lines_expressing: 36
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFITM2

*interferon induced transmembrane protein 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +4.4, q 0.007, up in 22 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.228× (z -11.9, q 8e-30, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFITM3]] (+0.91, fdr 7e-06, ⚠ same locus), [[IFITM1]] (+0.85, fdr 7e-06, ⚠ same locus), [[IFI6]] (+0.81, fdr 7e-06), [[BST2]] (+0.77, fdr 7e-06), [[IFI27]] (+0.77, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SP110]] → it (grade B ⚠); 7 go from it, the strongest it → [[TRIM38]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.14×** | +4.4 | 0.007 | 22/29 (HCT15, J82, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 1.77× | +3.2 | 0.45 | 15/26 (J82, PANC-1, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.228×** | -11.9 | 8e-30 | 33/34 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.349×** | -8.4 | 9e-15 | 31/34 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.296×** | -6.9 | 9e-10 | 28/33 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.310×** | -6.6 | 5e-09 | 32/33 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -6.4 | 1e-08 | 31/33 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.325×** | -6.4 | 2e-08 | 30/33 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.300×** | -5.8 | 5e-07 | 30/33 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.374×** | -5.6 | 2e-06 | 28/33 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.500×** | -5.5 | 2e-06 | 28/34 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.414×** | -5.0 | 3e-05 | 29/33 (SNU-423, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.456×** | -4.4 | 5e-04 | 28/33 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.457×** | -4.4 | 5e-04 | 26/33 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.459×** | -4.4 | 5e-04 | 25/33 (A549, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.595×** | -4.1 | 0.001 | 23/34 (BT-474, LoVo, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.487×** | -4.1 | 0.002 | 31/33 (BT-474, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.522×** | -3.7 | 0.009 | 26/33 (HepG2/C3A, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 95.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0605× (z -12.9) |
| [[RKO (line)]] | wt | 127 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.9) |
| [[C32 (line)]] | wt | 134 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0985× (z -10.0) |
| [[SW480 (line)]] | alt | 59.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -16.3) |
| [[A-172 (line)]] | wt | 51.7 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.322× (z -8.9) |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.188× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 73.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -8.9) |
| [[HCT15 (line)]] | alt | 63.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.4) |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.4) |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -14.8) |
| [[SNU-423 (line)]] | alt | 67.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.5) |
| [[A549 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.2) |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.8) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.223× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 69.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -9.7) |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.5) |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.4) |
| [[A-427 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFITM3]] | +0.91 | +0.71 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 805; ⚠ same locus (10.3 kb: neighbours can correlate without regulation) |
| [[IFITM1]] | +0.85 | +0.69 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 796; ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[IFI6]] | +0.81 | +0.60 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 674 |
| [[BST2]] | +0.77 | +0.63 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 615 |
| [[IFI27]] | +0.77 | +0.56 / +0.88 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 546 |
| [[UBE2L6]] | +0.75 | +0.54 / +0.83 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 435 |
| [[LY6E]] | +0.75 | +0.58 / +0.85 | both halves | 8e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 495 |
| [[OAS1]] | +0.73 | +0.54 / +0.81 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 594 |
| [[ISG15]] | +0.71 | +0.46 / +0.79 | both halves | 3e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 676 |
| [[MX2]] | +0.70 | +0.53 / +0.79 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 595 |
| [[SP110]] | +0.70 | +0.42 / +0.82 | both halves | 4e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[STAT1]] | +0.68 | +0.47 / +0.76 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 737 |
| [[HERC5]] | +0.68 | +0.50 / +0.75 | both halves | 1e-05 | pathway: Interferon Signaling; STRING 467 |
| [[USP18]] | +0.67 | +0.50 / +0.79 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SP110]] | B | SP110 activity raises IFITM2's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without SP110 | 0.060 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[TRIM38]] | B | TRIM38 activity raises IFITM2's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 3.87× lower at baseline in the lines without TRIM38 | 0.078 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[FGG]] | B | FGG activity raises IFITM2's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.33× lower at baseline in the lines without FGG | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM38]] | B | IFITM2 activity raises TRIM38's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without IFITM2 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[IFIT3]] | B | IFITM2 activity raises IFIT3's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 2.54× lower at baseline in the lines without IFITM2 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[SP100]] | B | IFITM2 activity raises SP100's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without IFITM2 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[PLEKHA4]] | B | IFITM2 activity raises PLEKHA4's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without IFITM2 | 0.087 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[GBP1]] | B | IFITM2 activity raises GBP1's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without IFITM2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[TMEM140]] | B | IFITM2 activity raises TMEM140's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without IFITM2 | 0.097 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[ZC3HAV1]] | B | IFITM2 activity raises ZC3HAV1's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without IFITM2 | 0.097 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 51.9); signed map (66.2, 29.3). **Vector** length 86.7, 30.4% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.66 to 23); *Interferon gamma signaling* (reactome, mean cos +0.56 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.60 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -8.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.3 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:303,655-309,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 1-8D, DSPA2c |
| Gene groups (HGNC) | Interferon induced transmembrane protein family; Dispanins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01629](https://www.uniprot.org/uniprotkb/Q01629) (Interferon-induced transmembrane protein 2):

> IFN-induced antiviral protein which inhibits the entry of viruses to the host cell cytoplasm, permitting endocytosis, but preventing subsequent viral fusion and release of viral contents into the cytosol. Active against multiple viruses, including influenza A virus, SARS coronaviruses (SARS-CoV and SARS-CoV-2), Marburg virus (MARV), Ebola virus (EBOV), Dengue virus (DNV), West Nile virus (WNV), human immunodeficiency virus type 1 (HIV-1), hepatitis C virus (HCV) and vesicular stomatitis virus …

**Summary**, from NCBI Gene [10581](https://www.ncbi.nlm.nih.gov/gene/10581):

> Interferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 and belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. [provided by RefSeq, Nov 2021]

**Accessions** — [HGNC:5413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5413) · Entrez [10581](https://www.ncbi.nlm.nih.gov/gene/10581) · UniProt [Q01629](https://www.uniprot.org/uniprotkb/Q01629) · Ensembl [ENSG00000185201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185201)

## Data

Gene col 11638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11638); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11638]; `tensor/DDL_lfc|DDL_z.npy` [11638]; `embed/gene_vectors.npy` [11638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11638 or target_col == 11638). Every well: [[IFITM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFITM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
