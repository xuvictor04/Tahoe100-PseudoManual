---
symbol: "SLC2A12"
type: "gene"
col: 7091
ensembl_id: "ENSG00000146411"
name: "solute carrier family 2 member 12"
location: "6q23.2"
module: 8
arm: "+"
pooled_cpm: 9.19
n_lines_expressing: 40
n_dd_up: 24
n_dd_down: 34
n_dd_up_clean: 21
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC2A12

*solute carrier family 2 member 12* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.79× (z +9.4, q 3e-18, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.269× (z -15.0, q 0e+00, down in 32 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.472× (z -8.6, q 3e-15, down in 23 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNMT]] (+0.57, fdr 2e-05), [[TMPRSS3]] (+0.54, fdr 3e-05), [[GBP2]] (+0.54, fdr 2e-05); moves opposite to [[SHLD2]] (-0.51, fdr 1e-05), [[ECPAS]] (-0.49, fdr 3e-05), [[LINC02987]] (-0.48, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C15orf48]] → it (grade B ⚠); 2 go from it, the strongest it → [[C15orf48]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +9.4 | 3e-18 | 25/37 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.6 | 1e-08 | 17/36 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.80×** | +6.5 | 2e-08 | 19/36 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +6.1 | 1e-07 | 20/37 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +6.0 | 2e-07 | 19/37 (PANC-1, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 3e-06 | 18/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 2e-05 | 17/37 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 3e-04 | 12/37 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.3 | 0.001 | 3/12 (SW1417, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.2 | 0.002 | 12/29 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +4.0 | 0.003 | 6/37 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 11/37 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 13/37 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.006 | 10/37 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 10/37 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 11/37 (KATO III, HT-29, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.021 | 12/37 (NCI-H2030, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.269×** | -15.0 | 0e+00 | 32/37 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -8.6 | 3e-15 | 23/37 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -8.4 | 6e-15 | 23/35 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -8.4 | 6e-15 | 23/30 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -7.1 | 1e-10 | 23/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -6.4 | 2e-08 | 21/37 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.347×** | -6.3 | 2e-08 | 23/35 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -6.2 | 5e-08 | 19/34 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.395×** | -5.5 | 2e-06 | 15/32 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.617×** | -5.5 | 2e-06 | 19/37 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.512×** | -5.4 | 3e-06 | 17/37 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.604×** | -5.4 | 3e-06 | 17/35 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -4.9 | 4e-05 | 16/37 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -4.8 | 7e-05 | 20/34 (COLO 205, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.669×** | -4.6 | 2e-04 | 15/36 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[EX229 (drug)]] 5 µM |  | **0.472×** | -4.5 | 3e-04 | 14/32 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.001 | 14/37 (CHP-212, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.702×** | -4.0 | 0.002 | 15/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.9 | 7 (1 ⚠) | 5 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 5.26× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -12.5) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 27.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -11.3) |
| [[COLO 205 (line)]] | alt | 147 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0627× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +8.7) ⚠ position not correctable | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0814× (z -15.1) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0592× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 5.80 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0854× (z -12.9) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.104× (z -11.4) |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -19.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -11.9) |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0550× (z -14.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0376× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 7.05 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0779× (z -10.3) |
| [[SW 900 (line)]] | alt | 7.92 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0939× (z -8.9) |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -9.4) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0756× (z -9.1) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 6.67 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.123× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 8.03 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0284× (z -10.0) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 5.05 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -8.8) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 9.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0729× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0607× (z -9.5) |
| [[RKO (line)]] | wt | 6.72 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0936× (z -8.5) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 5.87 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0880× (z -8.5) |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNMT]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TMPRSS3]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[GBP2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[BMF]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SLC7A8]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 | pathway: SLC-mediated transmembrane transport |
| [[SLC40A1]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 | pathway: SLC-mediated transmembrane transport |
| [[RBM47]] | +0.51 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[TNFSF10]] | +0.50 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[BTN3A2]] | +0.50 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[MTUS1]] | +0.50 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[B2M]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[POU3F2]] | +0.49 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHLD2]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ECPAS]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[LINC02987]] | -0.48 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[VAV2]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CCM2]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PARVB]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZBED4]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ATP6V0A2]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[RABEPK]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NLN]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PYGB]] | -0.45 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CAPN15]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity raises SLC2A12's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without C15orf48 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC2A12's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PPM1H]] | B | PPM1H activity raises SLC2A12's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without PPM1H | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[HNMT]] | B | HNMT activity raises SLC2A12's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without HNMT | 0.089 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | SLC2A12 activity raises C15orf48's level | lines that do not express SLC2A12 (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without SLC2A12 | 0.022 | ⚠ within organs, on part of the lines; also absent: IRAK2, IL22RA1, PLEKHG4; maybe low, not absent |
| [[WDR27]] | B | SLC2A12 activity raises WDR27's level | lines that do not express SLC2A12 (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without SLC2A12 | 0.078 | ⚠ within organs, on part of the lines; also absent: IRAK2, IL22RA1, PLEKHG4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, 50.0); signed map (64.4, -2.0). **Vector** length 73.7, 14.6% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -15.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:133,987,581-134,052,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT12, GLUT8 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD20](https://www.uniprot.org/uniprotkb/Q8TD20) (Solute carrier family 2, facilitated glucose transporter member 12):

> Insulin-independent facilitative glucose transporter.

**Summary**, from NCBI Gene [154091](https://www.ncbi.nlm.nih.gov/gene/154091):

> SLC2A12 belongs to a family of transporters that catalyze the uptake of sugars through facilitated diffusion (Rogers et al., 2002). This family of transporters show conservation of 12 transmembrane helices as well as functionally significant amino acid residues (Joost and Thorens, 2001 [PubMed 11780753]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18067) · Entrez [154091](https://www.ncbi.nlm.nih.gov/gene/154091) · UniProt [Q8TD20](https://www.uniprot.org/uniprotkb/Q8TD20) · Ensembl [ENSG00000146411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146411)

## Data

Gene col 7091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7091); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7091]; `tensor/DDL_lfc|DDL_z.npy` [7091]; `embed/gene_vectors.npy` [7091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7091 or target_col == 7091). Every well: [[SLC2A12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
