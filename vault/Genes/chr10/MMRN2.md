---
symbol: "MMRN2"
type: "gene"
col: 10366
ensembl_id: "ENSG00000173269"
name: "multimerin 2"
location: "10q23.2"
module: 80
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 39
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# MMRN2

*multimerin 2* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.34× (z +31.0, q 0e+00, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM: 0.588× (z -5.5, q 2e-05, down in 15 of 34 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.595× (z -5.4, q 2e-05, down in 12 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NANOS3]] (+0.77, fdr 7e-06), [[ENO3]] (+0.73, fdr 1e-05), [[LPXN]] (+0.70, fdr 7e-06); moves opposite to [[TTLL5]] (-0.63, fdr 3e-05), [[TAF5L]] (-0.62, fdr 1e-05), [[TYW1]] (-0.62, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRAF1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[STK11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.34×** | +31.0 | 0e+00 | 30/30 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.04×** | +13.8 | 4e-41 | 28/32 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.45×** | +12.8 | 5e-35 | 25/31 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +11.2 | 7e-27 | 19/29 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +11.1 | 2e-26 | 7/8 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.91×** | +9.4 | 5e-19 | 18/34 (A498, H4, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +9.0 | 2e-17 | 6/10 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.9 | 5e-17 | 11/18 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +6.5 | 6e-09 | 19/34 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.4 | 3e-06 | 11/34 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.3 | 6e-06 | 15/32 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.1 | 1e-05 | 6/18 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 12/33 (KATO III, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.3 | 7e-04 | 9/33 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.9 | 0.004 | 7/24 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +3.7 | 0.006 | 10/31 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.021 | 4/35 (A498, A-172, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.026 | 8/34 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.067 | 6/28 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.588×** | -5.5 | 2e-05 | 15/34 (H4, A549, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -5.4 | 2e-05 | 12/33 (HT-29, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Megestrol (drug)]] 5 µM |  | **0.694×** | -5.4 | 2e-05 | 17/35 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.472×** | -4.1 | 0.007 | 11/25 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.686×** | -3.9 | 0.011 | 10/33 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.710×** | -3.5 | 0.036 | 11/34 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.743× | -3.1 | 0.16 | 4/32 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.88 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +17.2) | — |
| [[A-172 (line)]] | wt | 7.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +16.7) | — |
| [[HS-578T (line)]] | alt | 3.76 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +15.0) | — |
| [[SW48 (line)]] | wt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.0) | — |
| [[C32 (line)]] | wt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +11.6) | — |
| [[H4 (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 9.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 6.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +17.0) | — |
| [[KATO III (line)]] | alt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +9.8) | — |
| [[LoVo (line)]] | wt | 2.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 3.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 5.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +9.1) | — |
| [[SW480 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +14.5) | — |
| [[A-427 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.983 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NANOS3]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ENO3]] | +0.73 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[LPXN]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[IL34]] | +0.69 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PIK3IP1-DT]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MSANTD3-TMEFF1]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[KDM6B]] | +0.68 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TRIM8]] | +0.68 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LETM2]] | +0.67 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[COL11A2]] | +0.66 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[PPP1R1C]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.62 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TYW1]] | -0.62 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[IQCB1]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ATRN]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GNB2]] | -0.61 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[RPA1]] | -0.61 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[NUP85]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SAP130]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GTF2E2]] | -0.60 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF1]] | B | TRAF1 activity raises MMRN2's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TRAF1 | 0.040 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[S100A3]] | B | S100A3 activity raises MMRN2's level | lines that do not express S100A3 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without S100A3 | 0.057 | ⚠ within organs, on part of the lines; also absent: S100A4; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MMRN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK11]] | B | MMRN2 activity raises STK11's level | lines that do not express MMRN2 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without MMRN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000225751 |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 9.6); signed map (25.0, 6.9). **Vector** length 66.9, 13.2% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +31.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.8 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.4 | -3.5 |
|  | [[NG25 (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | multimerin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:86,935,540-86,969,481 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EndoGlyx-1, FLJ13465; previously EMILIN3 |
| Gene groups (HGNC) | EMI domain containing; C1q domain containing |
| Reactome | 1 pathways, smallest: O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8L6](https://www.uniprot.org/uniprotkb/Q9H8L6) (Multimerin-2):

> Extracellular matrix protein. Affects several essential steps in angiogenesis including endothelial cell proliferation, migration, and tube formation. Positively regulates angiogenesis by acting as a ligand for CD93 receptor.

**Summary**, from NCBI Gene [79812](https://www.ncbi.nlm.nih.gov/gene/79812):

> This gene encodes a protein belonging to the member of elastin microfibril interface-located (EMILIN) protein family. This family member is an extracellular matrix glycoprotein that can interfere with tumor angiogenesis and growth. It serves as a transforming growth factor beta antagonist and can interfere with the VEGF-A/VEGFR2 pathway. A related pseudogene has been identified on chromosome 6. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:19888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19888) · Entrez [79812](https://www.ncbi.nlm.nih.gov/gene/79812) · UniProt [Q9H8L6](https://www.uniprot.org/uniprotkb/Q9H8L6) · Ensembl [ENSG00000173269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173269)

## Data

Gene col 10366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10366); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10366]; `tensor/DDL_lfc|DDL_z.npy` [10366]; `embed/gene_vectors.npy` [10366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10366 or target_col == 10366). Every well: [[MMRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
