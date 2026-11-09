---
symbol: "BEGAIN"
type: "gene"
col: 11369
ensembl_id: "ENSG00000183092"
name: "brain enriched guanylate kinase associated"
location: "14q32.2"
module: 110
arm: "+"
pooled_cpm: 11.56
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 15
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# BEGAIN

*brain enriched guanylate kinase associated* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.97× (z +8.4, q 2e-14, up in 12 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.59× (z +5.8, q 2e-06, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.380× (z -12.0, q 2e-30, down in 22 of 23 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACP7]] (+0.57, fdr 1e-05), [[LINC02509]] (+0.54, fdr 6e-05), [[NKAIN1]] (+0.51, fdr 1e-04); moves opposite to [[TBC1D23]] (-0.53, fdr 4e-05), [[COPB1]] (-0.46, fdr 2e-04), [[TRIQK]] (-0.45, fdr 9e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CBFA2T3]] → it (grade C ⚠); 15 go from it, the strongest it → [[SEH1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.4 | 2e-14 | 12/23 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +5.8 | 2e-06 | 13/24 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 2e-06 | 14/23 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 0.001 | 12/23 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.023 | 1/20 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.023 | 6/23 (SW480, AN3 CA, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.081 | 4/21 (SW480, LoVo, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.2 | 0.091 | 2/16 (SW480, HOP62) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.59× | +3.0 | 0.17 | 2/20 (SW480, SW48) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -12.0 | 2e-30 | 22/23 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.394×** | -11.6 | 2e-28 | 21/24 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.401×** | -11.3 | 2e-27 | 23/24 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.592×** | -9.2 | 5e-18 | 17/20 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.519×** | -8.1 | 5e-14 | 17/24 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -6.4 | 2e-08 | 18/24 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.389×** | -6.1 | 8e-08 | 14/24 (NCI-H460, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.636×** | -5.4 | 5e-06 | 11/22 (NCI-H2030, SW48, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -5.1 | 2e-05 | 14/23 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.713×** | -4.0 | 0.004 | 9/22 (SW48, H4, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.004 | 8/23 (SW480, SW48, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.006 | 12/24 (RKO, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.006 | 5/24 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.741×** | -3.7 | 0.008 | 8/23 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.008 | 8/23 (RKO, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 57.2 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0679× (z -15.9) |
| [[RKO (line)]] | wt | 24.8 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0285× (z -18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0540× (z -16.1) |
| [[SW480 (line)]] | alt | 7.15 | 4 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 8.87× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 7.26× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.203× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 57.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0625× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 88.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0712× (z -14.9) |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.1) |
| [[LoVo (line)]] | wt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.145× (z -10.5) |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -10.2) |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.5) |
| [[A549 (line)]] | wt | 5.31 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HOP62 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.431× (z -12.3) ⚠ position not correctable |
| [[LS 180 (line)]] | wt | 8.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 5.51 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.67× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0736× (z -12.7) |
| [[A-172 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP7]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LINC02509]] | +0.54 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[NKAIN1]] | +0.51 | +0.39 / +0.35 | both halves | 1e-04 |  |
| [[RBPMS2]] | +0.49 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[ADCY3]] | +0.48 | +0.54 / +0.32 | both halves | 2e-04 | pathway: Neuronal System |
| [[ELFN1]] | +0.47 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[EXD3]] | +0.47 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[ARHGEF4]] | +0.47 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PALD1]] | +0.47 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[SLC4A7]] | +0.46 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[PRDM15]] | +0.46 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[WT1-AS]] | +0.45 | +0.25 / +0.50 | both halves | 4e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D23]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[COPB1]] | -0.46 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[TRIQK]] | -0.45 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[SKIC3]] | -0.45 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[DSTN]] | -0.44 | -0.37 / -0.29 | both halves | 3e-04 |  |
| [[GRAMD2B]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PHKB]] | -0.44 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[SH3GLB1]] | -0.43 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[VIRMA]] | -0.42 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[UFSP2]] | -0.42 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[PTEN]] | -0.42 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TMCO1]] | -0.42 | -0.47 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T3]] | C | CBFA2T3 activity raises BEGAIN's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 3.20× lower at baseline in the lines without CBFA2T3 | 0.007 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEH1L]] | B | BEGAIN activity raises SEH1L's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without BEGAIN | 0.009 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[SH3GLB1]] | B | BEGAIN activity lowers SH3GLB1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.40× higher at baseline in the lines without BEGAIN | 0.012 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[PRDM15]] | B | BEGAIN activity raises PRDM15's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.36× lower at baseline in the lines without BEGAIN | 0.036 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[IGSF9B]] | B | BEGAIN activity raises IGSF9B's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without BEGAIN | 0.042 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[ELFN1]] | B | BEGAIN activity raises ELFN1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without BEGAIN | 0.043 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[BRSK2]] | B | BEGAIN activity raises BRSK2's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without BEGAIN | 0.053 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[P2RX5]] | B | BEGAIN activity raises P2RX5's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without BEGAIN | 0.059 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[ANKRD13B]] | B | BEGAIN activity raises ANKRD13B's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without BEGAIN | 0.074 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[CAPN15]] | B | BEGAIN activity raises CAPN15's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without BEGAIN | 0.079 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[GBX1]] | B | BEGAIN activity raises GBX1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without BEGAIN | 0.091 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[NKAIN1]] | B | BEGAIN activity raises NKAIN1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without BEGAIN | 0.095 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[WT1-AS]] | B | BEGAIN activity raises WT1-AS's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without BEGAIN | 0.098 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, 3.4); signed map (7.1, 56.4). **Vector** length 64.4, 15.9% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.2 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[NG25 (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | brain enriched guanylate kinase associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:100,537,147-100,587,417 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1446 |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUH8](https://www.uniprot.org/uniprotkb/Q9BUH8) (Brain-enriched guanylate kinase-associated protein):

> May sustain the structure of the postsynaptic density (PSD).

**Summary**, from NCBI Gene [57596](https://www.ncbi.nlm.nih.gov/gene/57596):

> Predicted to enable kinase activity. Predicted to be involved in evoked excitatory postsynaptic potential. Predicted to be located in dendrite; nucleus; and presynapse. Predicted to be active in glutamatergic synapse and postsynapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24163) · Entrez [57596](https://www.ncbi.nlm.nih.gov/gene/57596) · UniProt [Q9BUH8](https://www.uniprot.org/uniprotkb/Q9BUH8) · Ensembl [ENSG00000183092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183092)

## Data

Gene col 11369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11369); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11369]; `tensor/DDL_lfc|DDL_z.npy` [11369]; `embed/gene_vectors.npy` [11369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11369 or target_col == 11369). Every well: [[BEGAIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEGAIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
