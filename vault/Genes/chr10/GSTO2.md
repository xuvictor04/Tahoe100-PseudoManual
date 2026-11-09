---
symbol: "GSTO2"
type: "gene"
col: 800
ensembl_id: "ENSG00000065621"
name: "glutathione S-transferase omega 2"
location: "10q25.1"
module: 1
arm: "+"
pooled_cpm: 18.69
n_lines_expressing: 40
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GSTO2

*glutathione S-transferase omega 2* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.54× (z +7.5, q 4e-11, up in 11 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.41× (z +5.7, q 3e-06, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.402× (z -15.0, q 0e+00, down in 29 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -14.9, q 0e+00, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1D]] (+0.57, fdr 1e-05), [[SULT1A1]] (+0.56, fdr 2e-05), [[DCPS]] (+0.54, fdr 3e-05); moves opposite to [[MYL6]] (-0.56, fdr 2e-05), [[RTL8C]] (-0.54, fdr 5e-05), [[SMPD1]] (-0.52, fdr 3e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ILDR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.5 | 4e-11 | 11/25 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.3 | 8e-11 | 20/32 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.7 | 3e-06 | 18/36 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.0 | 1e-04 | 12/30 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 2e-04 | 12/37 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.60×** | +4.5 | 7e-04 | 6/34 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.009 | 8/37 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.017 | 11/36 (KATO III, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.025 | 11/36 (LoVo, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.5 | 0.025 | 11/37 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.026 | 8/36 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.057 | 6/38 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.057 | 2/37 (NCI-H23, AsPC-1) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.10 | 4/36 (KATO III, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -15.0 | 0e+00 | 29/36 (NCI-H2030, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -14.9 | 0e+00 | 29/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -13.0 | 2e-36 | 30/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -10.9 | 2e-25 | 27/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.717×** | -8.5 | 3e-15 | 21/35 (PANC-1, COLO 205, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -8.3 | 1e-14 | 25/36 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -6.9 | 3e-10 | 20/37 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -5.4 | 4e-06 | 20/37 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -5.3 | 7e-06 | 16/37 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -5.3 | 7e-06 | 19/35 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.757×** | -4.8 | 8e-05 | 17/36 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.767×** | -4.6 | 2e-04 | 13/32 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.784×** | -4.4 | 5e-04 | 12/37 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -4.2 | 9e-04 | 16/37 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.006 | 9/36 (SW48, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.030 | 11/36 (PANC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.6 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -19.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -17.4) |
| [[SW480 (line)]] | alt | 31.7 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -15.3) |
| [[LoVo (line)]] | wt | 38.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -12.4) |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -9.6) |
| [[HCT15 (line)]] | alt | 40.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.277× (z -8.5) |
| [[A-427 (line)]] | wt | 42.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.333× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.288× (z -11.0) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.0) |
| [[BT-474 (line)]] | alt | 4.90 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0663× (z -8.5) |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0992× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0649× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.243× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0985× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -10.8) |
| [[SW48 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1D]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SULT1A1]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 | pathway: Biological oxidations |
| [[DCPS]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[GPR143]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[CHDH]] | +0.52 | +0.59 / +0.41 | both halves | 4e-05 | same gene group |
| [[SHLD1]] | +0.52 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[SP2-AS1]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SPIN3]] | +0.52 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[COPG2IT1]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CCNT2]] | +0.51 | +0.50 / +0.23 | both halves | 5e-04 |  |
| [[CRACR2A]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[HSD17B2-AS1]] | +0.50 | +0.50 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL6]] | -0.56 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RTL8C]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[SMPD1]] | -0.52 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[GNB2]] | -0.49 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[LRPAP1]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[GNA11]] | -0.48 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ATG9A]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[GNAI2]] | -0.48 | -0.56 / -0.32 | both halves | 1e-04 |  |
| [[HMG20B]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NLGN2]] | -0.47 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[TMEM50A]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[FAM89B]] | -0.45 | -0.57 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ILDR1]] | B | ILDR1 activity raises GSTO2's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without ILDR1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[NMNAT3]] | B | NMNAT3 activity raises GSTO2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.76× lower at baseline in the lines without NMNAT3 | 0.072 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[COPG2IT1]] | B | COPG2IT1 activity raises GSTO2's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 2.14× lower at baseline in the lines without COPG2IT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (25.7, -40.2); signed map (17.6, -48.3). **Vector** length 66.1, 12.7% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.0 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -14.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -13.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -15.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase omega 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,268,873-104,304,950 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Soluble glutathione S-transferases; Oxidoreductases |
| Reactome | 6 pathways, smallest: Vitamin C (ascorbate) metabolism; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4Y5](https://www.uniprot.org/uniprotkb/Q9H4Y5) (Glutathione S-transferase omega-2):

> Exhibits glutathione-dependent thiol transferase activity. Has high dehydroascorbate reductase activity and may contribute to the recycling of ascorbic acid. Participates in the biotransformation of inorganic arsenic and reduces monomethylarsonic acid (MMA).

**Summary**, from NCBI Gene [119391](https://www.ncbi.nlm.nih.gov/gene/119391):

> The protein encoded by this gene is an omega class glutathione S-transferase (GST). GSTs are involved in the metabolism of xenobiotics and carcinogens. Four transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:23064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23064) · Entrez [119391](https://www.ncbi.nlm.nih.gov/gene/119391) · UniProt [Q9H4Y5](https://www.uniprot.org/uniprotkb/Q9H4Y5) · Ensembl [ENSG00000065621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065621)

## Data

Gene col 800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 800); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 800]; `tensor/DDL_lfc|DDL_z.npy` [800]; `embed/gene_vectors.npy` [800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 800 or target_col == 800). Every well: [[GSTO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
