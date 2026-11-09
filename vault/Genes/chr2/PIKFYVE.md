---
symbol: "PIKFYVE"
type: "gene"
col: 3614
ensembl_id: "ENSG00000115020"
name: "phosphoinositide kinase, FYVE-type zinc finger containing"
location: "2q34"
module: 30
arm: "+"
pooled_cpm: 135.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PIKFYVE

*phosphoinositide kinase, FYVE-type zinc finger containing* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.45× (z +5.4, q 4e-05, up in 30 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.41× (z +4.9, q 3e-04, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.440× (z -12.3, q 5e-32, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.745× (z -6.2, q 6e-08, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF1]] (+0.68, fdr 7e-06), [[COG5]] (+0.59, fdr 1e-04), [[MPST]] (+0.59, fdr 2e-04); moves opposite to [[PATL2]] (-0.59, fdr 1e-04), [[ANKRD18A]] (-0.58, fdr 4e-05), [[ZNF764]] (-0.57, fdr 7e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KITLG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.4 | 4e-05 | 30/47 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.9 | 3e-04 | 37/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.011 | 28/48 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.012 | 27/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.064 | 27/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.064 | 27/49 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.440×** | -12.3 | 5e-32 | 44/49 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -11.5 | 3e-28 | 42/44 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.509×** | -9.4 | 2e-18 | 42/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -6.2 | 6e-08 | 31/49 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -5.6 | 2e-06 | 38/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.707×** | -5.0 | 5e-05 | 35/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -4.6 | 4e-04 | 33/47 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.776×** | -3.8 | 0.010 | 30/48 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -3.7 | 0.013 | 26/48 (A498, A-172, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.648×** | -3.2 | 0.086 | 27/48 (RKO, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 192 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.9) |
| [[A-172 (line)]] | wt | 120 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 154 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 98.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.7) |
| [[C32 (line)]] | wt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -14.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 130 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +9.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.420× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 142 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 148 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.26× (z +9.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.239× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -14.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 77.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 86.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.416× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 154 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.25× (z +9.0) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 84.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 163 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -14.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 82.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.35× (z +9.1) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 73.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.08× (z +9.0) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -15.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0579× (z -14.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0883× (z -9.4) |
| [[SW 1271 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 106 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF1]] | +0.68 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[COG5]] | +0.59 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[MPST]] | +0.59 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[SACM1L]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | pathway: PI Metabolism |
| [[RNF41]] | +0.59 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[NUBP2]] | +0.58 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[RAB12]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TSNAX]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ERLEC1]] | +0.58 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ZCCHC17]] | +0.58 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.57 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[MPG]] | +0.57 | +0.57 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | -0.59 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD18A]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.57 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[PIEZO1]] | -0.56 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.56 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[WARS2-AS1]] | -0.55 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ZC3H4]] | -0.55 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PDCL3P4]] | -0.54 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[NANOS3]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF629]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD18B]] | -0.53 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KITLG]] | B | KITLG activity lowers PIKFYVE's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.31× higher at baseline in the lines without KITLG | 0.008 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers PIKFYVE's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers PIKFYVE's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKRD18B]] | B | ANKRD18B activity raises PIKFYVE's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without ANKRD18B | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.4, -16.6); signed map (-38.4, 3.1). **Vector** length 111, 38.8% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide kinase, FYVE-type zinc finger containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:208,266,255-208,358,746 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40423, KIAA0981, PIP5K, p235, ZFYVE29, FAB1; previously PIP5K3 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; DEP domain containing; Phosphoinositide kinase, FYVE-type zinc finger containing family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I7](https://www.uniprot.org/uniprotkb/Q9Y2I7) (1-phosphatidylinositol 3-phosphate 5-kinase):

> Dual specificity kinase implicated in myriad essential cellular processes such as maintenance of endomembrane homeostasis, and endocytic-vacuolar pathway, lysosomal trafficking, nuclear transport, stress- or hormone-induced signaling and cell cycle progression. The PI(3,5)P2 regulatory complex regulates both the synthesis and turnover of phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2). Sole enzyme to catalyze the phosphorylation of phosphatidylinositol 3-phosphate on the fifth hydroxyl of …

**Summary**, from NCBI Gene [200576](https://www.ncbi.nlm.nih.gov/gene/200576):

> Phosphorylated derivatives of phosphatidylinositol (PtdIns) regulate cytoskeletal functions, membrane trafficking, and receptor signaling by recruiting protein complexes to cell- and endosomal-membranes. Humans have multiple PtdIns proteins that differ by the degree and position of phosphorylation of the inositol ring. This gene encodes an enzyme (PIKfyve; also known as phosphatidylinositol-3-phosphate 5-kinase type III or PIPKIII) that phosphorylates the D-5 position in PtdIns and …

**Accessions** — [HGNC:23785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23785) · Entrez [200576](https://www.ncbi.nlm.nih.gov/gene/200576) · UniProt [Q9Y2I7](https://www.uniprot.org/uniprotkb/Q9Y2I7) · Ensembl [ENSG00000115020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115020)

## Data

Gene col 3614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3614); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3614]; `tensor/DDL_lfc|DDL_z.npy` [3614]; `embed/gene_vectors.npy` [3614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3614 or target_col == 3614). Every well: [[PIKFYVE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIKFYVE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
