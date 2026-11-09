---
symbol: "MICU3"
type: "gene"
col: 7935
ensembl_id: "ENSG00000155970"
name: "mitochondrial calcium uptake 3"
location: "8p22"
module: 16
arm: "+"
pooled_cpm: 24.16
n_lines_expressing: 31
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MICU3

*mitochondrial calcium uptake 3* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.50× (z +5.4, q 4e-05, up in 18 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.296× (z -15.6, q 0e+00, down in 20 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.494× (z -12.6, q 5e-34, down in 26 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK1]] (+0.57, fdr 3e-05), [[KIAA0408]] (+0.54, fdr 3e-05), [[ZFP1]] (+0.53, fdr 3e-05); moves opposite to [[TTC41P]] (-0.48, fdr 2e-04), [[GAL3ST2]] (-0.47, fdr 1e-04), [[ADAM10]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MPDZ]] → it (grade C ⚠); 3 go from it, the strongest it → [[PDGFC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 4e-05 | 18/29 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.1 | 8e-05 | 18/29 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.033 | 12/29 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.059 | 8/29 (HS-578T, NCI-H460, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.27× | +3.2 | 0.15 | 8/29 (HS-578T, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.1 | 0.15 | 14/29 (HS-578T, A-427, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.26× | +3.1 | 0.15 | 11/29 (A-427, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.296×** | -15.6 | 0e+00 | 20/22 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.389×** | -12.6 | 5e-34 | 25/28 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -12.6 | 5e-34 | 26/29 (CHP-212, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.389×** | -11.6 | 5e-29 | 20/26 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.464×** | -9.8 | 1e-20 | 26/28 (NCI-H460, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.516×** | -8.8 | 1e-16 | 21/28 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.529×** | -8.5 | 2e-15 | 22/29 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -8.2 | 2e-14 | 22/29 (A-427, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -8.2 | 2e-14 | 21/29 (A-427, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -8.1 | 4e-14 | 21/29 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.599×** | -6.6 | 2e-09 | 19/29 (A-172, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.620×** | -6.4 | 9e-09 | 21/29 (NCI-H460, SW 1271, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.668×** | -5.4 | 3e-06 | 18/28 (H4, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.680×** | -5.1 | 1e-05 | 15/29 (A-427, A-172, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.713×** | -4.5 | 2e-04 | 15/29 (NCI-H460, A-172, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -4.5 | 3e-04 | 16/28 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -3.0 | 0.064 | 11/28 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.732×** | -3.0 | 0.076 | 10/29 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.076 | 10/29 (HepG2/C3A, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 125 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0688× (z -24.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.123× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 31.2 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0731× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.357× (z -8.5) |
| [[A-172 (line)]] | wt | 84.2 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -12.1) |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -9.0) |
| [[A498 (line)]] | wt | 39.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -8.6) |
| [[SNU-423 (line)]] | alt | 32.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.0) |
| [[HS-578T (line)]] | alt | 65.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0491× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.4) |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 60.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0578× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 57.1 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -11.3) ⚠ transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0719× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -8.6) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0743× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 24.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0622× (z -8.5) |
| [[CHP-212 (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 46.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.331× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -8.9) |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK1]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[KIAA0408]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZFP1]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[MIR3171HG]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ZNF354C]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SOGA3]] | +0.50 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ZNF197]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CERS4]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZFHX4]] | +0.48 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[MARCHF7]] | +0.48 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[ZSCAN12]] | +0.48 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[ZFP37]] | +0.48 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC41P]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[GAL3ST2]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ADAM10]] | -0.47 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[DNM2]] | -0.47 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ITGA9-AS1]] | -0.46 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[DNAJB11]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[DNAJC3]] | -0.45 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[TM9SF3]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[BCAR3-AS1]] | -0.44 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[STK24]] | -0.43 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[LINC02656]] | -0.43 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[GTPBP1]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPDZ]] | C | MPDZ activity raises MICU3's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 8.07× lower at baseline in the lines without MPDZ | 0.047 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[ZNF354C]] | C | ZNF354C activity raises MICU3's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 4.59× lower at baseline in the lines without ZNF354C | 0.049 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |
| [[ZFP82]] | C | ZFP82 activity raises MICU3's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 5.97× lower at baseline in the lines without ZFP82 | 0.086 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFC]] | B | MICU3 activity raises PDGFC's level | lines that do not express MICU3 (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without MICU3 | 0.029 | ⚠ within organs, on part of the lines; co-absent genes; also absent: BVES-AS1, EVL, MIR130AHG |
| [[BCAR3-AS1]] | B | MICU3 activity lowers BCAR3-AS1's level | lines that do not express MICU3 (19) vs lines expressing it (31) | 1.52× higher at baseline in the lines without MICU3 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: BVES-AS1, EVL, MIR130AHG |
| [[ZFP82]] | C | MICU3 activity raises ZFP82's level | lines that do not express MICU3 (19) vs lines expressing it (31) | 5.15× lower at baseline in the lines without MICU3 | 0.049 | ⚠ within organs, on part of the lines; co-absent genes; also absent: BVES-AS1, EVL, MIR130AHG; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.6, 23.7); signed map (-4.0, -31.6). **Vector** length 70.0, 17.7% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | -2.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.0 | -6.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -8.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.2 | +0.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial calcium uptake 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,027,238-17,122,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313A0139; previously EFHA2 |
| Gene groups (HGNC) | EF-hand domain containing; MCU complex subunits |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XE3](https://www.uniprot.org/uniprotkb/Q86XE3) (Calcium uptake protein 3, mitochondrial):

> Tissue-specific calcium sensor of the mitochondrial calcium uniporter (MCU) channel, which specifically regulates MCU channel activity in the central nervous system and skeletal muscle. Senses calcium level via its EF-hand domains: compared to MICU1 and MICU2, MICU3 has a higher affinity for calcium. MICU1 and MICU3 form a disulfide-linked heterodimer that stimulates and inhibits MCU activity, depending on the concentration of calcium. At low calcium levels, MICU1 occludes the pore of the MCU …

**Summary**, from NCBI Gene [286097](https://www.ncbi.nlm.nih.gov/gene/286097):

> Enables calcium ion sensor activity and protein heterodimerization activity. Involved in calcium import into the mitochondrion and cellular response to calcium ion. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27820) · Entrez [286097](https://www.ncbi.nlm.nih.gov/gene/286097) · UniProt [Q86XE3](https://www.uniprot.org/uniprotkb/Q86XE3) · Ensembl [ENSG00000155970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155970)

## Data

Gene col 7935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7935); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7935]; `tensor/DDL_lfc|DDL_z.npy` [7935]; `embed/gene_vectors.npy` [7935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7935 or target_col == 7935). Every well: [[MICU3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICU3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
