---
symbol: "BCAS4"
type: "gene"
col: 4510
ensembl_id: "ENSG00000124243"
name: "breast carcinoma amplified sequence 4"
location: "20q13.13"
module: 30
arm: "+"
pooled_cpm: 18.42
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# BCAS4

*breast carcinoma amplified sequence 4* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +10.7, q 7e-24, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.584× (z -8.1, q 5e-13, down in 28 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.609× (z -7.7, q 3e-12, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3BP5]] (+0.67, fdr 7e-06), [[WDFY1]] (+0.61, fdr 1e-05), [[EML2]] (+0.61, fdr 1e-05); moves opposite to [[TRIP12]] (-0.59, fdr 1e-05), [[XRCC5]] (-0.55, fdr 1e-05), [[C2CD3]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGFR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +10.7 | 7e-24 | 40/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +9.2 | 8e-18 | 33/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.2 | 1e-10 | 30/46 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.3 | 5e-08 | 26/45 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.5 | 5e-06 | 24/46 (BT-474, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +5.4 | 5e-06 | 23/46 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 22/46 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 2e-04 | 15/44 (BT-474, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 18/46 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +4.4 | 6e-04 | 18/45 (BT-474, PANC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.002 | 14/46 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 17/45 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 9/46 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +3.9 | 0.004 | 12/46 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 16/45 (BT-474, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.007 | 12/46 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.010 | 19/46 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -8.1 | 5e-13 | 28/43 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.609×** | -7.7 | 3e-12 | 28/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -6.2 | 1e-07 | 20/45 (HCT15, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.684×** | -5.9 | 5e-07 | 26/44 (LS 180, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.692×** | -5.7 | 1e-06 | 24/45 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.774×** | -4.0 | 0.006 | 14/45 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.8 | 0.013 | 4/46 (SW 1271, SHP-77, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.859× | -3.3 | 0.056 | 10/46 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.807×** | -3.3 | 0.056 | 15/46 (HOP62, A549, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.861× | -3.3 | 0.057 | 12/46 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.819×** | -3.1 | 0.099 | 7/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.5 | 6 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 6.94× (z +11.3) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 7.15× (z +11.0) | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.9) |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 2 | — | [[Arbutin (drug)]] 5 µM 0.0789× (z -9.8) |
| [[LoVo (line)]] | wt | 10.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -8.8) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0705× (z -9.1) |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0965× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.9) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.316× (z -8.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.108× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 8.38 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0699× (z -8.6) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0660× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.7) |
| [[RKO (line)]] | wt | 23.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BP5]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[WDFY1]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[EML2]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PKN1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MIR193BHG]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LACTB]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ENTREP1]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[GPR160]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RGPD8]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[C2CD3]] | -0.54 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[CFAP44]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CDKN2B-AS1]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SRCAP]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[XNDC1N]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PRH1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[STAG1]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF407]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[KIAA0825]] | -0.50 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGFR1]] | B | FGFR1 activity raises BCAS4's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.47× lower at baseline in the lines without FGFR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[HRK]] | B | HRK activity raises BCAS4's level | lines that do not express HRK (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without HRK | 0.037 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[TCF7L1]] | B | TCF7L1 activity raises BCAS4's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without TCF7L1 | 0.048 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[PIK3CD]] | B | PIK3CD activity raises BCAS4's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without PIK3CD | 0.052 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[EPHA10]] | B | EPHA10 activity strengthens BCAS4's drug response | lines that do not express EPHA10 (18) vs lines expressing it (28) | the lines without EPHA10 respond 0.58× as strongly (z diff +1.21); rises at some drug-doses, falls at others (41% from rises): Ouabain (Octahydrate) 0.5 µM: 0.94x vs 0.54x (z diff +2.8); Ouabain (Octahydrate) 5 µM: 0.87x vs 0.50x (z diff +2.8); Belinostat 5 µM: 1.41x vs 1.80x (z diff +1.2) | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (8.2, -10.6); signed map (-26.8, -4.9). **Vector** length 95.4, 20.6% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +4.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -3.1 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | breast carcinoma amplified sequence 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,794,894-50,877,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20495, CNOL |
| Matched by | ensembl_id |

UniProt [Q8TDM0](https://www.uniprot.org/uniprotkb/Q8TDM0) carries no function annotation.

**Summary**, from NCBI Gene [55653](https://www.ncbi.nlm.nih.gov/gene/55653):

> Predicted to be located in cytoplasm. Predicted to be part of BLOC-1 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14367) · Entrez [55653](https://www.ncbi.nlm.nih.gov/gene/55653) · UniProt [Q8TDM0](https://www.uniprot.org/uniprotkb/Q8TDM0) · Ensembl [ENSG00000124243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124243)

## Data

Gene col 4510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4510); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4510]; `tensor/DDL_lfc|DDL_z.npy` [4510]; `embed/gene_vectors.npy` [4510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4510 or target_col == 4510). Every well: [[BCAS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
