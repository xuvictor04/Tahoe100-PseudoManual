---
symbol: "CCDC191"
type: "gene"
col: 8731
ensembl_id: "ENSG00000163617"
name: "coiled-coil domain containing 191"
location: "3q13.31"
module: 10
arm: "+"
pooled_cpm: 25.93
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 36
n_dd_up_clean: 6
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCDC191

*coiled-coil domain containing 191* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 0.5 µM: 1.50× (z +4.5, q 0.003, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.218× (z -16.9, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC2]] (+0.71, fdr 7e-06), [[SPATA17]] (+0.65, fdr 7e-06), [[C11orf65]] (+0.63, fdr 3e-05); moves opposite to [[KLHL29]] (-0.51, fdr 5e-05), [[EXTL3]] (-0.51, fdr 5e-05), [[CPOX]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FBXO15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 0.003 | 25/46 (SW480, A-427, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.003 | 24/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 0.003 | 28/47 (KATO III, CHP-212, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.013 | 23/46 (NCI-H23, SW480, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.069 | 13/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +3.3 | 0.083 | 19/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.083 | 14/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | 1.72× | +3.1 | 0.12 | 14/47 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 11/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.12 | 14/47 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.218×** | -16.9 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.220×** | -16.7 | 0e+00 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.278×** | -14.1 | 4e-43 | 46/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.338×** | -12.0 | 6e-31 | 42/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.390×** | -10.0 | 2e-21 | 39/45 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.425×** | -9.4 | 3e-19 | 37/46 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.483×** | -8.0 | 8e-14 | 37/46 (HT-29, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.501×** | -7.2 | 3e-11 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.288×** | -7.2 | 4e-11 | 35/45 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.637×** | -7.0 | 1e-10 | 28/46 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -6.6 | 2e-09 | 35/47 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.665×** | -6.4 | 9e-09 | 36/47 (hTERT-HPNE, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -6.3 | 1e-08 | 29/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -6.2 | 2e-08 | 25/46 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.572×** | -6.2 | 3e-08 | 29/47 (PANC-1, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -5.1 | 1e-05 | 27/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.649×** | -4.8 | 6e-05 | 22/46 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -4.7 | 6e-05 | 30/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.467×** | -4.4 | 3e-04 | 21/45 (SNU-1, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 51.3 | 0 | 15 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0659× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.100× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -12.6) |
| [[A-427 (line)]] | wt | 63.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.100× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 50.0 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -17.3) |
| [[SW480 (line)]] | alt | 23.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -14.3) |
| [[COLO 205 (line)]] | alt | 46.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.2) |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.104× (z -14.5) |
| [[A549 (line)]] | wt | 31.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.257× (z -8.6) |
| [[HOP62 (line)]] | alt | 33.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 27.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0961× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 5 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0333× (z -10.5) |
| [[SNU-423 (line)]] | alt | 30.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -9.3) |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -10.7) |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -11.1) |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -10.1) |
| [[J82 (line)]] | alt | 19.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.149× (z -8.6) |
| [[A-172 (line)]] | wt | 47.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0797× (z -10.7) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.237× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0567× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -9.6) |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -9.8) |
| [[C32 (line)]] | wt | 14.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0636× (z -11.0) |
| [[H4 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0537× (z -12.0) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -11.2) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.191× (z -9.4) |
| [[LoVo (line)]] | wt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -8.6) |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -9.3) |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC2]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SPATA17]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[C11orf65]] | +0.63 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[CARF]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[EFCAB6]] | +0.59 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SUMF1]] | +0.57 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[WDR31]] | +0.57 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[DRC3]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[AK8]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC27]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SLC24A1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TTC12]] | +0.55 | +0.63 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | -0.51 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[EXTL3]] | -0.51 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[CPOX]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CACNB4]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TMEM181]] | -0.45 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[PRRG1]] | -0.45 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SMCO4]] | -0.44 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TMEM184B]] | -0.44 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[UNC5A]] | -0.44 | -0.26 / -0.53 | both halves | 3e-04 |  |
| [[SCD5]] | -0.44 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[ATP11A]] | -0.43 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CCDC168]] | -0.43 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO15]] | B | FBXO15 activity raises CCDC191's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without FBXO15 | 0.068 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CCDC191's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[MORN1]] | C | MORN1's natural level strengthens CCDC191's drug response | MORN1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.25; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFT81]] | C | IFT81's natural level strengthens CCDC191's drug response | IFT81's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SPATA17]] | C | SPATA17 activity raises CCDC191's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.5, 27.5); signed map (3.0, 4.8). **Vector** length 74.1, 19.5% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.0 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +4.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 191 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:113,964,137-114,056,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1407 |
| Matched by | ensembl_id |

UniProt [Q8NCU4](https://www.uniprot.org/uniprotkb/Q8NCU4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29272) · Entrez [57577](https://www.ncbi.nlm.nih.gov/gene/57577) · UniProt [Q8NCU4](https://www.uniprot.org/uniprotkb/Q8NCU4) · Ensembl [ENSG00000163617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163617)

## Data

Gene col 8731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8731); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8731]; `tensor/DDL_lfc|DDL_z.npy` [8731]; `embed/gene_vectors.npy` [8731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8731 or target_col == 8731). Every well: [[CCDC191 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC191.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
