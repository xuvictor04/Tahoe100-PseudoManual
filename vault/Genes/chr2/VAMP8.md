---
symbol: "VAMP8"
type: "gene"
col: 4009
ensembl_id: "ENSG00000118640"
name: "vesicle associated membrane protein 8"
location: "2p11.2"
module: 24
arm: "+"
pooled_cpm: 17.63
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# VAMP8

*vesicle associated membrane protein 8* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.32× (z +13.3, q 9e-38, up in 30 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 13 lines (HOP62 32.1×, HEC-1-A 7.38×, NCI-H23 14.4×, HT-29 7.64×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.52×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.628× (z -3.7, q 0.065, down in 22 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID4B]] (+0.62, fdr 4e-05), [[VAMP5]] (+0.62, fdr 1e-05, ⚠ same locus), [[SMIM27]] (+0.61, fdr 1e-05), [[C1orf56]] (+0.61, fdr 4e-05); moves opposite to [[FARSB]] (-0.59, fdr 3e-05), [[COA1]] (-0.56, fdr 3e-05), [[BOP1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[VAMP5]] → it (grade B ⚠); 7 go from it, the strongest it → [[VAMP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4009.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 13 lines (HOP62 32.1×, HEC-1-A 7.38×, NCI-H23 14.4×, HT-29 7.64×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.52×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.32×** | +13.3 | 9e-38 | 30/34 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.1 | 1e-13 | 28/30 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +7.2 | 8e-11 | 20/24 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +5.2 | 3e-05 | 14/26 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.7 | 4e-04 | 26/33 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.6 | 5e-04 | 19/34 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.065 | 22/34 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -3.7 | 0.065 | 23/34 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -3.5 | 0.081 | 19/33 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.647× | -3.2 | 0.17 | 21/34 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.672× | -3.2 | 0.17 | 22/34 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.759× | -3.1 | 0.17 | 19/33 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 26.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.83× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 48.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.9) |
| [[HCT15 (line)]] | alt | 22.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.29× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.38× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 4.57 | 1 | 0 | [[Auranofin (drug)]] 5 µM 32.1× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 29.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.64× (z +11.1) | — |
| [[LoVo (line)]] | wt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.12× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.2× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 9.18 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.4× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 5.78 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 7.21 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.8× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 9.43 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.64× (z +8.9) | — |
| [[SW48 (line)]] | wt | 15.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +9.3) | — |
| [[SW480 (line)]] | alt | 21.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.77× (z +10.8) | — |
| [[A-172 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[VAMP5]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 771; ⚠ same locus (2.4 kb, same strand: neighbours can correlate without regulation) |
| [[SMIM27]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[C11orf1]] | +0.60 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[CCDC142]] | +0.59 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[ZNF846]] | +0.59 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[FMC1]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LANCL1-AS1]] | +0.57 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[BMPR2]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NAA38]] | +0.56 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[APOC1]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TSC22D4]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[COA1]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[BOP1]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TRAP1]] | -0.52 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[MTG1]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PAICS]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CEP83]] | -0.52 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[TCOF1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[LAS1L]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP5]] | B | VAMP5 activity raises VAMP8's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 3.21× lower at baseline in the lines without VAMP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[WFDC2]] | B | WFDC2 activity raises VAMP8's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without WFDC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[CRIP1]] | B | CRIP1 activity raises VAMP8's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without CRIP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[C11orf52]] | B | C11orf52 activity raises VAMP8's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without C11orf52 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[HDAC6]] | B | HDAC6 activity raises VAMP8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FCGRT]] | B | FCGRT activity raises VAMP8's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without FCGRT | 0.059 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[WFDC2]] | B | WFDC2 activity strengthens VAMP8's drug response | lines that do not express WFDC2 (24) vs lines expressing it (10) | the lines without WFDC2 respond 0.88× as strongly (z diff +0.23); strongest at Panobinostat 5 µM: 0.67x vs 0.45x (z diff +2.5) | 0.097 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; both ways; artifact flags |
| [[RHOD]] | C | RHOD activity raises VAMP8's level | lines that do not express RHOD (15) vs lines expressing it (35) | 3.09× lower at baseline in the lines without RHOD | 0.040 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1; co-absent with the target |
| [[GPRC5C]] | C | GPRC5C activity raises VAMP8's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without GPRC5C | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP5]] | B | VAMP8 activity raises VAMP5's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without VAMP8 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[PRRG2]] | B | VAMP8 activity raises PRRG2's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without VAMP8 | 0.053 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[HOXA-AS2]] | B | VAMP8 activity raises HOXA-AS2's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without VAMP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| cells under [[Torkinib (drug)]] 5 µM | B | VAMP8 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express VAMP8 (14) vs lines expressing it (34) | the lines without VAMP8: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[FCGRT]] | B | VAMP8 activity raises FCGRT's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.94× lower at baseline in the lines without VAMP8 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[GPRC5C]] | C | VAMP8 activity raises GPRC5C's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without VAMP8 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent; co-absent with the target |
| [[RHOD]] | C | VAMP8 activity raises RHOD's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 3.34× lower at baseline in the lines without VAMP8 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.6, 25.5); signed map (-6.2, 3.1). **Vector** length 57.6, 15.6% of its response variance represented; |z| ≥ 3 in 368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,561,562-85,582,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EDB, VAMP-8 |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, P53_PATHWAY |
| Reactome | 13 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV40](https://www.uniprot.org/uniprotkb/Q9BV40) (Vesicle-associated membrane protein 8):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). VAMP8 is a v-SNARE that …

**Summary**, from NCBI Gene [8673](https://www.ncbi.nlm.nih.gov/gene/8673):

> This gene encodes an integral membrane protein that belongs to the synaptobrevin/vesicle-associated membrane protein subfamily of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs). The encoded protein is involved in the fusion of synaptic vesicles with the presynaptic membrane.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:12647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12647) · Entrez [8673](https://www.ncbi.nlm.nih.gov/gene/8673) · UniProt [Q9BV40](https://www.uniprot.org/uniprotkb/Q9BV40) · Ensembl [ENSG00000118640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118640)

## Data

Gene col 4009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4009); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4009]; `tensor/DDL_lfc|DDL_z.npy` [4009]; `embed/gene_vectors.npy` [4009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4009 or target_col == 4009). Every well: [[VAMP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
