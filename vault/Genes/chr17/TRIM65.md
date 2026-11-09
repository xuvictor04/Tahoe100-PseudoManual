---
symbol: "TRIM65"
type: "gene"
col: 6549
ensembl_id: "ENSG00000141569"
name: "tripartite motif containing 65"
location: "17q25.1"
module: 5
arm: "+"
pooled_cpm: 12.52
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRIM65

*tripartite motif containing 65* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.22× (z +3.9, q 0.047, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.503× (z -9.6, q 3e-19, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P2RX5]] (+0.65, fdr 7e-06), [[ENTR1]] (+0.65, fdr 8e-06), [[PUS1]] (+0.64, fdr 7e-06); moves opposite to [[ADD3]] (-0.60, fdr 1e-05), [[FAAH2]] (-0.52, fdr 1e-05), [[ATP6V1A]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC25A15]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.047 | 15/45 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.081 | 16/42 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.081 | 14/44 (HCT15, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.081 | 11/47 (SW480, HOP62, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.081 | 14/45 (C-33 A, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.083 | 12/45 (SW480, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.15 | 8/42 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.15 | 11/44 (SW48, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.23× | +3.0 | 0.17 | 5/47 (SW480, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.503×** | -9.6 | 3e-19 | 30/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.645×** | -8.7 | 1e-15 | 29/47 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -7.4 | 2e-11 | 29/47 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.595×** | -7.0 | 4e-10 | 28/46 (PANC-1, J82, …) | top dose only | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -6.9 | 6e-10 | 23/47 (A-427, PANC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -6.6 | 3e-09 | 26/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -6.5 | 7e-09 | 20/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.642×** | -6.2 | 4e-08 | 26/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.463×** | -5.7 | 1e-06 | 20/42 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.673×** | -5.5 | 2e-06 | 21/47 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.684×** | -5.3 | 5e-06 | 20/47 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.696×** | -5.1 | 2e-05 | 19/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.689×** | -5.0 | 2e-05 | 12/22 (SW480, MIA PaCa-2, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.704×** | -4.9 | 4e-05 | 22/45 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -4.8 | 5e-05 | 24/47 (KATO III, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -4.6 | 2e-04 | 19/44 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -4.5 | 2e-04 | 15/47 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -3.6 | 0.009 | 17/47 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.620×** | -3.5 | 0.012 | 12/48 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.056 | 13/48 (C-33 A, J82, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.058 | 7/47 (A-427, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -12.6) |
| [[A-172 (line)]] | wt | 21.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.7) |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0908× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.104× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0453× (z -9.6) |
| [[A549 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 5.56 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0890× (z -9.0) |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.120× (z -10.1) ⚠ cell-cycle shift, explains ~10% of this change |
| [[J82 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 4.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -9.6) |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0603× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0924× (z -10.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW480 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RX5]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ENTR1]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[PUS1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[LRFN4]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZNF276]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ULK3]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[DDX51]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[INPP5E]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CPNE7]] | +0.62 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.61 | +0.60 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRM1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NOP2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MED22]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADD3]] | -0.60 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[FAAH2]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ATP6V1A]] | -0.51 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MAGT1]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[VAMP7]] | -0.51 | -0.43 / -0.52 | both halves | 4e-05 |  |
| [[GOLM2]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[DNAH7]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SRP14]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[GALM]] | -0.50 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[GDE1]] | -0.50 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[DSTN]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises TRIM65's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NT5M | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[FAAH2]] | B | FAAH2 activity lowers TRIM65's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.35× higher at baseline in the lines without FAAH2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[NT5M]] | B | NT5M activity strengthens TRIM65's drug response | lines that do not express NT5M (7) vs lines expressing it (41) | the lines without NT5M respond 0.42× as strongly (z diff +1.78); strongest at Panobinostat 5 µM: 1.10x vs 0.60x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[HSF2BP]] | C | HSF2BP activity raises TRIM65's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without HSF2BP | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A15]] | C | TRIM65's natural level strengthens SLC25A15's drug response | TRIM65's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.44; direction not clear | 0.087 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.2, -30.4); signed map (1.2, -49.9). **Vector** length 73.0, 12.4% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -9.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 65 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,880,335-75,896,951 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJ69](https://www.uniprot.org/uniprotkb/Q6PJ69) (E3 ubiquitin-protein ligase TRIM65):

> E3 ubiquitin ligase that plays a role in several processes including innate immnity, autophagy or inflammation. Negatively regulates miRNAs by modulating the ubiquitination and stability of TNRC6A, a protein involved in RNA-mediated gene silencing by both micro-RNAs (miRNAs) and short interfering RNAs. This ubiquitination results in the suppressed expression of miR-138-5p leading to increased autophagy. Upon enteroviral infection, promotes 'Lys-63'-mediated ubiquitination activation of …

**Summary**, from NCBI Gene [201292](https://www.ncbi.nlm.nih.gov/gene/201292):

> Enables protein domain specific binding activity and ubiquitin protein ligase activity. Involved in several processes, including positive regulation of interferon-beta production; protein K48-linked ubiquitination; and regulation of defense response. Acts upstream of or within innate immune response; positive regulation of protein oligomerization; and protein K63-linked ubiquitination. Located in cytosol and nucleoplasm. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun …

**Accessions** — [HGNC:27316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27316) · Entrez [201292](https://www.ncbi.nlm.nih.gov/gene/201292) · UniProt [Q6PJ69](https://www.uniprot.org/uniprotkb/Q6PJ69) · Ensembl [ENSG00000141569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141569)

## Data

Gene col 6549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6549); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6549]; `tensor/DDL_lfc|DDL_z.npy` [6549]; `embed/gene_vectors.npy` [6549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6549 or target_col == 6549). Every well: [[TRIM65 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM65.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
