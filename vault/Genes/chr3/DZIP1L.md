---
symbol: "DZIP1L"
type: "gene"
col: 8139
ensembl_id: "ENSG00000158163"
name: "DAZ interacting zinc finger protein 1 like"
location: "3q22.3"
module: 31
arm: "+"
pooled_cpm: 16.54
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 21
direction_downstream: 28
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# DZIP1L

*DAZ interacting zinc finger protein 1 like* — 3q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.375× (z -9.6, q 4e-19, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDST1]] (+0.58, fdr 3e-05), [[RHOBTB1]] (+0.58, fdr 1e-04), [[MDFIC]] (+0.57, fdr 6e-05); moves opposite to [[TMC4]] (-0.55, fdr 3e-05), [[MYO1D]] (-0.54, fdr 4e-05), [[TMEM45B]] (-0.52, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TMEM45B]] → it (grade B ⚠); 28 go from it, the strongest it → [[PLCG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.41× | +3.2 | 0.44 | 13/39 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.26× | +3.2 | 0.44 | 8/40 (HS-578T, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -9.6 | 4e-19 | 32/40 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.395×** | -9.1 | 2e-17 | 30/40 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.529×** | -8.8 | 2e-16 | 31/39 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -8.2 | 3e-14 | 27/40 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -7.2 | 5e-11 | 24/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.485×** | -6.8 | 8e-10 | 26/40 (HOP62, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.512×** | -6.6 | 4e-09 | 23/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.581×** | -5.3 | 7e-06 | 24/37 (SNU-1, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -5.3 | 8e-06 | 23/40 (A-427, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -5.1 | 2e-05 | 20/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.588×** | -5.0 | 3e-05 | 16/24 (MIA PaCa-2, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.604×** | -5.0 | 3e-05 | 20/34 (hTERT-HPNE, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.614×** | -4.8 | 8e-05 | 24/37 (SNU-1, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.710×** | -4.8 | 8e-05 | 29/40 (LoVo, SW 1271, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.617×** | -4.4 | 4e-04 | 14/30 (AN3 CA, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -3.8 | 0.005 | 20/40 (NCI-H1792, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -3.7 | 0.005 | 20/40 (SW 900, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -3.7 | 0.005 | 19/39 (H4, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -3.2 | 0.032 | 15/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.731×** | -3.1 | 0.053 | 15/40 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.057 | 14/40 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.166× (z -11.8) |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.209× (z -10.0) |
| [[HS-578T (line)]] | alt | 45.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0856× (z -13.7) |
| [[A-172 (line)]] | wt | 33.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.4) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.7) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.189× (z -9.2) |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -10.0) |
| [[A-427 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0831× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 30.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H1573 (line)]] | alt | 8.90 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -11.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -9.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDST1]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RHOBTB1]] | +0.58 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[MDFIC]] | +0.57 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[COL5A2]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[ARHGEF6]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[AKAP7]] | +0.55 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[POGLUT3]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SIRPA]] | +0.55 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[CPQ]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ITGA4]] | +0.51 | +0.51 / +0.27 | both halves | 3e-04 |  |
| [[SMPD4]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CNTLN]] | +0.50 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC4]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MYO1D]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TMEM45B]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ADCY4]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PATJ]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[FAM83E]] | -0.48 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[RDH13]] | -0.47 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[LINC02649]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ERN1]] | -0.46 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[UBE2B]] | -0.45 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[FAAH2]] | -0.45 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[CATSPER2]] | -0.45 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45B]] | B | TMEM45B activity lowers DZIP1L's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.15× higher at baseline in the lines without TMEM45B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[ESRP1]] | B | ESRP1 activity lowers DZIP1L's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.63× higher at baseline in the lines without ESRP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[FGD1]] | B | FGD1 activity raises DZIP1L's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.91× lower at baseline in the lines without FGD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[TMC4]] | B | TMC4 activity lowers DZIP1L's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.06× higher at baseline in the lines without TMC4 | 0.030 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[GRB7]] | B | GRB7 activity lowers DZIP1L's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.59× higher at baseline in the lines without GRB7 | 0.037 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[ANTXR1]] | B | ANTXR1 activity raises DZIP1L's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 3.21× lower at baseline in the lines without ANTXR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[FUT3]] | B | FUT3 activity lowers DZIP1L's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.70× higher at baseline in the lines without FUT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[SRPX]] | B | SRPX activity raises DZIP1L's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without SRPX | 0.067 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ARHGEF6]] | B | ARHGEF6 activity raises DZIP1L's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without ARHGEF6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[GLIS1]] | B | GLIS1 activity raises DZIP1L's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without GLIS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[OXCT1]] | B | OXCT1 activity raises DZIP1L's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without OXCT1 | 0.086 | ⚠ within organs, on part of the lines |
| [[FAAH2]] | B | FAAH2 activity lowers DZIP1L's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.08× higher at baseline in the lines without FAAH2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 22, C 6. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCG1]] | B | DZIP1L activity raises PLCG1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without DZIP1L | 0.007 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[TMEM45B]] | B | DZIP1L activity lowers TMEM45B's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 17.79× higher at baseline in the lines without DZIP1L | 0.007 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[NDST1]] | B | DZIP1L activity raises NDST1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without DZIP1L | 0.008 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[ADCY4]] | B | DZIP1L activity lowers ADCY4's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.74× higher at baseline in the lines without DZIP1L | 0.015 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[FOXM1]] | B | DZIP1L activity raises FOXM1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without DZIP1L | 0.015 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[PLCG1]] | B | DZIP1L activity weakens PLCG1's drug response | lines that do not express DZIP1L (8) vs lines expressing it (40) | the lines without DZIP1L respond 1.70× as strongly (z diff -1.75); strongest at Idarubicin (hydrochloride) 5 µM: 2.10x vs 1.31x (z diff -3.2) | 0.026 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CHST14]] | B | DZIP1L activity raises CHST14's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without DZIP1L | 0.037 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[FGD1]] | B | DZIP1L activity raises FGD1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.08× lower at baseline in the lines without DZIP1L | 0.040 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[CSTB]] | B | DZIP1L activity lowers CSTB's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.86× higher at baseline in the lines without DZIP1L | 0.043 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[FAM83E]] | B | DZIP1L activity lowers FAM83E's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 4.20× higher at baseline in the lines without DZIP1L | 0.044 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[DCLK2]] | B | DZIP1L activity raises DCLK2's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 5.44× lower at baseline in the lines without DZIP1L | 0.056 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[SCARA3]] | B | DZIP1L activity raises SCARA3's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without DZIP1L | 0.060 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction -0.379). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.1, 30.8); signed map (17.5, 23.0). **Vector** length 75.3, 16.0% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +1.9 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +1.8 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.0 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DAZ interacting zinc finger protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,061,990-138,115,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32844, DZIP2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYY4](https://www.uniprot.org/uniprotkb/Q8IYY4) (Cilium assembly protein DZIP1L):

> Involved in primary cilium formation. Probably acts as a transition zone protein required for localization of PKD1/PC1 and PKD2/PC2 to the ciliary membrane.

**Summary**, from NCBI Gene [199221](https://www.ncbi.nlm.nih.gov/gene/199221):

> Predicted to enable zinc ion binding activity. Involved in cilium assembly and regulation of protein localization. Located in centriole and ciliary basal body. Implicated in polycystic kidney disease 5. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26551) · Entrez [199221](https://www.ncbi.nlm.nih.gov/gene/199221) · UniProt [Q8IYY4](https://www.uniprot.org/uniprotkb/Q8IYY4) · Ensembl [ENSG00000158163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158163)

## Data

Gene col 8139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8139); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8139]; `tensor/DDL_lfc|DDL_z.npy` [8139]; `embed/gene_vectors.npy` [8139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8139 or target_col == 8139). Every well: [[DZIP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DZIP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
