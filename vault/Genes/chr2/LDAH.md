---
symbol: "LDAH"
type: "gene"
col: 4030
ensembl_id: "ENSG00000118961"
name: "lipid droplet associated hydrolase"
location: "2p24.1"
module: 1
arm: "+"
pooled_cpm: 32.89
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# LDAH

*lipid droplet associated hydrolase* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.25× (z +4.4, q 0.005, up in 22 of 46 measured lines) ⚠ cell-cycle shift, explains ~85% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.31× (z +3.7, q 0.037, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.363× (z -13.9, q 3e-41, down in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.364× (z -13.9, q 3e-41, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRRF]] (+0.82, fdr 7e-06), [[NOL8]] (+0.71, fdr 7e-06), [[ZNF507]] (+0.69, fdr 7e-06); moves opposite to [[CDK2AP2]] (-0.58, fdr 1e-04), [[TMEM184B]] (-0.58, fdr 1e-05), [[CARD19]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF480]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.25×** | +4.4 | 0.005 | 22/46 (HT-29, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.033 | 21/39 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.037 | 22/46 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.037 | 17/46 (NCI-H460, A-427, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.047 | 19/46 (RKO, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.047 | 12/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.062 | 16/45 (NCI-H460, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.062 | 14/46 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.081 | 11/46 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.091 | 12/46 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.13 | 11/46 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.363×** | -13.9 | 3e-41 | 41/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -13.9 | 3e-41 | 44/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -11.7 | 2e-29 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -11.7 | 2e-29 | 41/46 (SHP-77, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -9.0 | 2e-17 | 40/46 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.561×** | -7.9 | 2e-13 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.593×** | -6.9 | 5e-10 | 31/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.601×** | -6.7 | 1e-09 | 30/46 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.599×** | -6.6 | 2e-09 | 27/46 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.735×** | -5.9 | 2e-07 | 30/46 (SK-MEL-2, SW1417, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -5.4 | 3e-06 | 26/46 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -4.8 | 6e-05 | 29/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.718×** | -4.4 | 6e-04 | 24/46 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.546×** | -4.3 | 6e-04 | 23/41 (SHP-77, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.561×** | -4.1 | 0.001 | 23/46 (SHP-77, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.726×** | -3.1 | 0.050 | 13/46 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -3.0 | 0.075 | 15/46 (CFPAC-1, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.287× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 46.7 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -11.6) |
| [[SW480 (line)]] | alt | 49.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.0) |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -19.1) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.221× (z -10.6) |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -11.2) |
| [[SHP-77 (line)]] | alt | 53.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -17.6) |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -9.4) |
| [[LoVo (line)]] | wt | 27.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 25.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -9.0) |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -11.4) |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -13.1) |
| [[A-427 (line)]] | wt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.269× (z -9.9) |
| [[CHP-212 (line)]] | wt | 57.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0390× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -9.5) |
| [[H4 (line)]] | wt | 26.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0708× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 34.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.8) |
| [[A549 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[C32 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.9) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -8.8) |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 22.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.9) |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRRF]] | +0.82 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[NOL8]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[USP40]] | +0.68 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[GUF1]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RRP15]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SLX4IP]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[JPX]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[FKTN]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ACBD6]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[GATB]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP2]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.58 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CARD19]] | -0.57 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[INPP5A]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NOL4L]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CCNYL1]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF480]] | C | ZNF480 activity raises LDAH's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without ZNF480 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.5, 6.6); signed map (4.7, -38.7). **Vector** length 80.1, 18.9% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Pimitespib (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | lipid droplet associated hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,684,014-20,823,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21820; previously C2orf43 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6V9](https://www.uniprot.org/uniprotkb/Q9H6V9) (Lipid droplet-associated hydrolase):

> Probable serine lipid hydrolase associated with lipid droplets (By similarity). Has low cholesterol esterase activity (By similarity). Appears to lack triglyceride lipase activity (By similarity). Involved in cholesterol and triglyceride homeostasis; has opposing effects, stimulating cellular triglyceride accumulation and cellular cholesterol release. Acts antagonistically with PNPLA2/ATGL in regulation of cellular lipid stores. May regulate triglyceride accumulation indirectly through …

**Summary**, from NCBI Gene [60526](https://www.ncbi.nlm.nih.gov/gene/60526):

> Predicted to enable sterol ester esterase activity. Involved in cholesterol homeostasis and intracellular triglyceride homeostasis. Acts upstream of with a positive effect on lipid droplet fusion. Located in endoplasmic reticulum and lipid droplet. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26145) · Entrez [60526](https://www.ncbi.nlm.nih.gov/gene/60526) · UniProt [Q9H6V9](https://www.uniprot.org/uniprotkb/Q9H6V9) · Ensembl [ENSG00000118961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118961)

## Data

Gene col 4030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4030); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4030]; `tensor/DDL_lfc|DDL_z.npy` [4030]; `embed/gene_vectors.npy` [4030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4030 or target_col == 4030). Every well: [[LDAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
