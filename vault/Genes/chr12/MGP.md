---
symbol: "MGP"
type: "gene"
col: 3223
ensembl_id: "ENSG00000111341"
name: "matrix Gla protein"
location: "12p12.3"
module: 104
arm: "+"
pooled_cpm: 6.33
n_lines_expressing: 15
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 16
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# MGP

*matrix Gla protein* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.23× (z +8.9, q 4e-16, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +4.1, q 0.007, up in 3 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Triamcinolone (drug)]] 5 µM in 1 line (HS-578T 10.1×); [[Dexamethasone (drug)]] 5 µM in 1 line (HS-578T 22.9×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0688×); [[Selinexor (drug)]] 5 µM in 1 line (BT-474 0.174×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCN]] (+0.66, fdr 1e-05), [[ENPP2]] (+0.65, fdr 1e-05), [[ITGA8]] (+0.64, fdr 1e-05); moves opposite to [[RDUR]] (-0.50, fdr 2e-05), [[LINC00973]] (-0.49, fdr 5e-05), [[KCNC4]] (-0.48, fdr 3e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LUM]] → it (grade C ⚠); 16 go from it, the strongest it → [[P2RX7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Triamcinolone (drug)]] 5 µM in 1 line (HS-578T 10.1×); [[Dexamethasone (drug)]] 5 µM in 1 line (HS-578T 22.9×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.23×** | +8.9 | 4e-16 | 3/4 (Hs 766T, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.37×** | +8.2 | 6e-14 | 6/8 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.75×** | +6.8 | 2e-09 | 3/5 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.007 | 3/9 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.6 | 0.033 | 2/10 (Hs 766T, AN3 CA) | top dose only | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.78× | +3.2 | 0.12 | 5/11 (NCI-H1792, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.76× | +3.1 | 0.13 | 4/10 (AN3 CA, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.74× | +3.1 | 0.13 | 2/8 (Hs 766T, HOP62) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.65× | +3.1 | 0.13 | 3/11 (C32, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0688×); [[Selinexor (drug)]] 5 µM in 1 line (BT-474 0.174×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.567× | -3.2 | 0.67 | 6/9 (AN3 CA, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.579× | -3.0 | 0.67 | 1/12 (RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 14.9 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 825 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0688× (z -20.0) |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.174× (z -8.6) |
| [[A-172 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.831 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCN]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 597 |
| [[ENPP2]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[ITGA8]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[TWIST1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CCN4]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATOH8]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HSD11B1]] | +0.56 | +0.41 / +0.62 | both halves | 4e-05 | **novel candidate** |
| [[RIPOR2]] | +0.56 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[TMTC1]] | +0.55 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[COL3A1]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 562 |
| [[DCT]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[NPR3]] | +0.51 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDUR]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[LINC00973]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[KCNC4]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[IL11]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PINLYP]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[LINC01812]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[TCP10L]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[EVA1A]] | -0.45 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[CSF2]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[LIF]] | -0.43 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[MIR4280HG]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[LINC02454]] | -0.42 | -0.38 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUM]] | C | LUM activity raises MGP's level | lines that do not express LUM (34) vs lines expressing it (16) | 1.81× lower at baseline in the lines without LUM | 0.082 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX7]] | B | MGP activity raises P2RX7's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without MGP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |
| [[RASA3]] | B | MGP activity raises RASA3's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without MGP | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |
| [[FKBP7]] | B | MGP activity raises FKBP7's level | lines that do not express MGP (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without MGP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |
| [[HTRA3]] | C | MGP activity raises HTRA3's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without MGP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[IL1B]] | C | MGP activity raises IL1B's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.97× lower at baseline in the lines without MGP | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[LOX]] | C | MGP activity raises LOX's level | lines that do not express MGP (35) vs lines expressing it (15) | 5.47× lower at baseline in the lines without MGP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[RPSAP52]] | C | MGP activity raises RPSAP52's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.50× lower at baseline in the lines without MGP | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[C1R]] | C | MGP activity raises C1R's level | lines that do not express MGP (35) vs lines expressing it (15) | 4.05× lower at baseline in the lines without MGP | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[SULF1]] | C | MGP activity raises SULF1's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.12× lower at baseline in the lines without MGP | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[LUM]] | C | MGP activity raises LUM's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without MGP | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[ENPP2]] | C | MGP activity raises ENPP2's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.87× lower at baseline in the lines without MGP | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[TF]] | C | MGP activity raises TF's level | lines that do not express MGP (35) vs lines expressing it (15) | 1.44× lower at baseline in the lines without MGP | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.7, 23.2); signed map (24.1, 38.3). **Vector** length 28.1, 6.87% of its response variance represented; |z| ≥ 3 in 264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | matrix Gla protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:14,880,864-14,885,857 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gla domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P08493](https://www.uniprot.org/uniprotkb/P08493) (Matrix Gla protein):

> Associates with the organic matrix of bone and cartilage. Thought to act as an inhibitor of bone formation.

**Summary**, from NCBI Gene [4256](https://www.ncbi.nlm.nih.gov/gene/4256):

> This gene encodes a member of the osteocalcin/matrix Gla family of proteins. The encoded vitamin K-dependent protein is secreted by chondrocytes and vascular smooth muscle cells, and functions as a physiological inhibitor of ectopic tissue calcification. Carboxylation status of the encoded protein is associated with calcification of the vasculature in human patients with cardiovascular disease and calcification of the synovial membranes in osteoarthritis patients. Mutations in this gene cause …

**Accessions** — [HGNC:7060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7060) · Entrez [4256](https://www.ncbi.nlm.nih.gov/gene/4256) · UniProt [P08493](https://www.uniprot.org/uniprotkb/P08493) · Ensembl [ENSG00000111341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111341)

## Data

Gene col 3223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3223); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3223]; `tensor/DDL_lfc|DDL_z.npy` [3223]; `embed/gene_vectors.npy` [3223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3223 or target_col == 3223). Every well: [[MGP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
