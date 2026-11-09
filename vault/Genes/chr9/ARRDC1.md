---
symbol: "ARRDC1"
type: "gene"
col: 12336
ensembl_id: "ENSG00000197070"
name: "arrestin domain containing 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 9.22
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ARRDC1

*arrestin domain containing 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.64× (z +6.6, q 3e-08, up in 16 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.35× (z +3.9, q 0.011, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.577× (z -7.3, q 1e-10, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKI]] (+0.60, fdr 1e-05), [[ERGIC1]] (+0.55, fdr 3e-05), [[NIBAN2]] (+0.53, fdr 3e-05); moves opposite to [[TLR1]] (-0.48, fdr 8e-05), [[HNMT]] (-0.47, fdr 4e-05), [[BTN3A3]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABLIM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +6.6 | 3e-08 | 16/29 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.5 | 1e-05 | 8/18 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.9 | 2e-04 | 11/25 (BT-474, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.011 | 12/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +3.6 | 0.028 | 9/47 (A498, NCI-H460, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +3.6 | 0.028 | 13/43 (RKO, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.028 | 5/36 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.028 | 13/45 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +3.5 | 0.028 | 8/39 (A498, RKO, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.043 | 6/45 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.065 | 14/44 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.088 | 5/41 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.096 | 14/45 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.0 | 0.096 | 4/37 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Torkinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.0 | 0.096 | 5/30 (RKO, HCT15, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -7.3 | 1e-10 | 30/47 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.384×** | -6.7 | 7e-09 | 24/45 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -6.0 | 4e-07 | 21/45 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -5.8 | 1e-06 | 22/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -5.6 | 3e-06 | 20/45 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.699×** | -4.8 | 2e-04 | 21/44 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -4.6 | 3e-04 | 17/41 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.788×** | -4.5 | 5e-04 | 19/41 (A549, A-172, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -4.5 | 5e-04 | 17/46 (SNU-423, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -4.1 | 0.002 | 20/41 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -3.8 | 0.007 | 13/46 (SW 1271, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.762×** | -3.6 | 0.013 | 10/47 (SW 1271, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.6 | 0.017 | 13/46 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.759×** | -3.5 | 0.021 | 7/45 (HS-578T, SW1417, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.029 | 13/43 (A549, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.063 | 14/46 (SW48, C-33 A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.792×** | -3.1 | 0.064 | 4/48 (SNU-1, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.0) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 5.83 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0635× (z -11.8) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 4.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0718× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.15 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0650× (z -11.7) |
| [[J82 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 2.96 | 0 | 1 | — | [[Dapagliflozin (drug)]] 0.05 µM 0.0513× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0895× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0647× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0463× (z -10.4) |
| [[SW48 (line)]] | wt | 9.92 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0782× (z -8.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKI]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[NIBAN2]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[MAP3K6]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PLSCR3]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[NRBP2]] | +0.52 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[CDC42BPB]] | +0.51 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[ACOT7]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CAPRIN2]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[POLG]] | +0.51 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[DVL1]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR1]] | -0.48 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[HNMT]] | -0.47 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[BTN3A3]] | -0.46 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[LRP1B]] | -0.45 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[TM4SF18]] | -0.44 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[MECOM]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[MMP13]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GCNT2]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TLR6]] | -0.43 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[CHIC1]] | -0.43 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ZSCAN31]] | -0.43 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[DOK5]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM2]] | B | ABLIM2 activity raises ARRDC1's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without ABLIM2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (32.4, 11.7); signed map (-12.6, 41.6). **Vector** length 65.2, 10.4% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.4 | +3.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +6.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +3.1 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | arrestin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,605,685-137,615,360 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40555 |
| Gene groups (HGNC) | Alpha arrestins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5I2](https://www.uniprot.org/uniprotkb/Q8N5I2) (Arrestin domain-containing protein 1):

> Functions as an adapter recruiting ubiquitin-protein ligases to their specific substrates. Through an ubiquitination-dependent mechanism plays for instance a role in the incorporation of SLC11A2 into extracellular vesicles. More generally, plays a role in the extracellular transport of proteins between cells through the release in the extracellular space of microvesicles. By participating in the ITCH-mediated ubiquitination and subsequent degradation of NOTCH1, negatively regulates the NOTCH …

**Summary**, from NCBI Gene [92714](https://www.ncbi.nlm.nih.gov/gene/92714):

> Enables several functions, including arrestin family protein binding activity; ubiquitin protein ligase binding activity; and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including extracellular transport; extracellular vesicle biogenesis; and negative regulation of Notch signaling pathway. Located in cytoplasmic vesicle; extracellular vesicle; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28633) · Entrez [92714](https://www.ncbi.nlm.nih.gov/gene/92714) · UniProt [Q8N5I2](https://www.uniprot.org/uniprotkb/Q8N5I2) · Ensembl [ENSG00000197070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197070)

## Data

Gene col 12336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12336); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12336]; `tensor/DDL_lfc|DDL_z.npy` [12336]; `embed/gene_vectors.npy` [12336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12336 or target_col == 12336). Every well: [[ARRDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
