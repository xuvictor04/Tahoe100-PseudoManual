---
symbol: "DLGAP1-AS1"
type: "gene"
col: 10813
ensembl_id: "ENSG00000177337"
name: "DLGAP1 antisense RNA 1"
location: "18p11.31"
module: 10
arm: "+"
pooled_cpm: 14.75
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 35
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# DLGAP1-AS1

*DLGAP1 antisense RNA 1* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.60× (z +6.6, q 2e-08, up in 17 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.42× (z +3.8, q 0.024, up in 7 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.376× (z -21.2, q 0e+00, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP1-AS2]] (+0.75, fdr 7e-06, ⚠ same locus), [[TM4SF1-AS1]] (+0.54, fdr 2e-05), [[TGIF1]] (+0.53, fdr 1e-05), [[GEM]] (+0.51, fdr 3e-05); moves opposite to [[PRKAR2A]] (-0.47, fdr 9e-05), [[APPL1]] (-0.42, fdr 3e-04), [[NKTR]] (-0.40, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CACNG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +6.6 | 2e-08 | 17/31 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.20×** | +4.0 | 0.015 | 14/46 (LOX-IMVI, HepG2/C3A, …) | rises with dose | low cells (technical?); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.024 | 7/41 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +3.5 | 0.056 | 11/43 (RKO, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.23× | +3.2 | 0.16 | 8/45 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.16 | 6/42 (A-172, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.376×** | -21.2 | 0e+00 | 36/45 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.281×** | -19.4 | 0e+00 | 41/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.306×** | -18.1 | 0e+00 | 41/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.404×** | -13.9 | 2e-41 | 40/46 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.415×** | -13.5 | 3e-39 | 34/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -10.9 | 1e-25 | 28/43 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.488×** | -10.6 | 3e-24 | 28/45 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.531×** | -9.7 | 3e-20 | 31/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -9.5 | 1e-19 | 30/44 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.606×** | -7.7 | 1e-12 | 28/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.617×** | -7.4 | 8e-12 | 27/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -7.2 | 3e-11 | 27/46 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -7.2 | 3e-11 | 27/41 (HT-29, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.1 | 3e-08 | 25/45 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -5.5 | 1e-06 | 22/41 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -5.3 | 5e-06 | 20/45 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM |  | **0.536×** | -5.0 | 2e-05 | 17/40 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -4.6 | 1e-04 | 9/43 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.4 | 3e-04 | 17/45 (NCI-H23, A-427, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.586×** | -4.3 | 4e-04 | 8/41 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.2 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -21.5) |
| [[NCI-H23 (line)]] | alt | 48.1 | 0 | 9 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0393× (z -22.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.3) |
| [[LoVo (line)]] | wt | 16.3 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0257× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -28.2) |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.1) |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0450× (z -13.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0672× (z -12.5) |
| [[SHP-77 (line)]] | alt | 7.72 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -12.1) |
| [[A549 (line)]] | wt | 13.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 20.9 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -10.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.2) |
| [[PANC-1 (line)]] | alt | 9.00 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -17.5) |
| [[A-427 (line)]] | wt | 64.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.6) |
| [[COLO 205 (line)]] | alt | 8.89 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0374× (z -12.1) |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -10.4) |
| [[KATO III (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.3) |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0600× (z -15.0) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -9.3) |
| [[C32 (line)]] | wt | 8.18 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.106× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0753× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 9.71 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0510× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 8.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.8) |
| [[RKO (line)]] | wt | 14.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 8.42 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[SW 900 (line)]] | alt | 8.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -10.6) |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 14 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP1-AS2]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TM4SF1-AS1]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[TGIF1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GEM]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ATXN1-AS1]] | +0.51 | +0.47 / +0.41 | both halves | 4e-05 | same gene group |
| [[SRP14-DT]] | +0.50 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[CACNG2]] | +0.49 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[LINC03042]] | +0.48 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[BEX2]] | +0.48 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[UBE2D3]] | +0.47 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[TLCD5]] | +0.46 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[MKLN1-AS]] | +0.46 | +0.34 / +0.43 | both halves | 1e-04 | same gene group |
| [[METTL27]] | +0.46 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR2A]] | -0.47 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[APPL1]] | -0.42 | -0.26 / -0.40 | both halves | 3e-04 |  |
| [[NKTR]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[GLT8D1]] | -0.40 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[ZHX3]] | -0.40 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[TTLL11]] | -0.40 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[HECTD4]] | -0.39 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[RMDN3]] | -0.38 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[NOMO3]] | -0.38 | -0.14 / -0.40 | ⚠ not reproduced | 0.002 |  |
| [[POLG]] | -0.38 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[TRAM2]] | -0.38 | -0.22 / -0.35 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG2]] | B | CACNG2 activity lowers DLGAP1-AS1's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.83× higher at baseline in the lines without CACNG2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[GEM]] | B | GEM activity lowers DLGAP1-AS1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.58× higher at baseline in the lines without GEM | 0.058 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[KLKP1-1]] | B | KLKP1-1 activity lowers DLGAP1-AS1's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.90× higher at baseline in the lines without KLKP1-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises DLGAP1-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without MIR1915HG | 0.096 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.277). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (32.0, 6.9); signed map (39.9, 2.8). **Vector** length 74.5, 14.2% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.5 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -19.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -18.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.1 | -13.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -7.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | DLGAP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.31 — chr18:3,593,732-3,598,363 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HsT914, FLJ35776 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31676) · Entrez [649446](https://www.ncbi.nlm.nih.gov/gene/649446) · Ensembl [ENSG00000177337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177337)

## Data

Gene col 10813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10813); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10813]; `tensor/DDL_lfc|DDL_z.npy` [10813]; `embed/gene_vectors.npy` [10813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10813 or target_col == 10813). Every well: [[DLGAP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
