---
symbol: "ZNF41"
type: "gene"
col: 7151
ensembl_id: "ENSG00000147124"
name: "zinc finger protein 41"
location: "Xp11.3"
module: 156
arm: "+"
pooled_cpm: 17.86
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# ZNF41

*zinc finger protein 41* — Xp11.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -10.4, q 1e-22, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.600× (z -7.5, q 4e-12, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF2]] (+0.61, fdr 1e-05), [[MOSMO]] (+0.59, fdr 1e-05), [[ZNF623]] (+0.58, fdr 2e-05); moves opposite to [[CXADR]] (-0.55, fdr 3e-05), [[VAT1]] (-0.54, fdr 4e-05), [[KIF13A]] (-0.54, fdr 2e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MGAT4A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.28× | +3.6 | 0.16 | 14/47 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.26 | 10/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.492×** | -10.4 | 1e-22 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.608×** | -10.3 | 1e-22 | 33/47 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.497×** | -10.3 | 1e-22 | 38/46 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.516×** | -9.7 | 3e-20 | 26/40 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.519×** | -8.9 | 5e-17 | 25/35 (MIA PaCa-2, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.561×** | -8.5 | 2e-15 | 34/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.581×** | -8.0 | 1e-13 | 27/48 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.598×** | -7.6 | 3e-12 | 32/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.600×** | -7.5 | 4e-12 | 32/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -7.2 | 3e-11 | 24/46 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -7.0 | 1e-10 | 29/44 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -6.2 | 2e-08 | 26/47 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -6.0 | 7e-08 | 26/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -6.0 | 7e-08 | 26/46 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.665×** | -6.0 | 8e-08 | 26/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.694×** | -5.3 | 3e-06 | 25/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -4.9 | 3e-05 | 23/46 (NCI-H2030, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -4.8 | 5e-05 | 20/47 (AN3 CA, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -4.3 | 4e-04 | 21/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.003 | 17/48 (CHP-212, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -3.3 | 0.020 | 17/44 (SW1417, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.022 | 6/47 (PANC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -2.8 | 0.087 | 13/48 (Hs 766T, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.3 | 0 | 11 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0850× (z -16.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.214× (z -10.0) |
| [[SW480 (line)]] | alt | 26.8 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -11.2) |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0348× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[C32 (line)]] | wt | 16.2 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.168× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -8.9) |
| [[J82 (line)]] | alt | 26.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.4) |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.173× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0473× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 | — | [[GSK1059615 (drug)]] 5 µM 0.0603× (z -10.1) |
| [[A498 (line)]] | wt | 7.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -16.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0827× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 6.06 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.146× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0747× (z -11.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.261× (z -8.6) |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MOSMO]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZNF623]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 | same gene group |
| [[ALG8]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SDHC]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DHRS7B]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF7]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 | same gene group |
| [[NACC1]] | +0.54 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[DUS2]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[WDR53]] | +0.54 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[CPSF3]] | +0.54 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[GON4L]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[VAT1]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KIF13A]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DSTN]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MAPRE2]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[LAMP2]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MLF1]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TWSG1]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[TKT]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TXNDC16]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SLC25A23]] | -0.49 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[KIAA2012]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT4A]] | B | MGAT4A activity lowers ZNF41's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without MGAT4A | 0.067 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.1, 3.3); signed map (-7.8, -22.3). **Vector** length 60.9, 9.95% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.4 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.3 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,445,178-47,483,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8941, MRX89 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P51814](https://www.uniprot.org/uniprotkb/P51814) (Zinc finger protein 41):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7592](https://www.ncbi.nlm.nih.gov/gene/7592):

> This gene encodes a protein that contains KRAB-A and KRAB-B domains multiple zinc finger DNA binding motifs and finger linking regions characteristic of the Kruppel family. An initial study suggested that this gene may be associated with X-linked cognitive disability, but a later study has called this finding into question (PMID:23871722).[provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:13107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13107) · Entrez [7592](https://www.ncbi.nlm.nih.gov/gene/7592) · UniProt [P51814](https://www.uniprot.org/uniprotkb/P51814) · Ensembl [ENSG00000147124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147124)

## Data

Gene col 7151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7151); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7151]; `tensor/DDL_lfc|DDL_z.npy` [7151]; `embed/gene_vectors.npy` [7151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7151 or target_col == 7151). Every well: [[ZNF41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
