---
symbol: "MBOAT1"
type: "gene"
col: 10223
ensembl_id: "ENSG00000172197"
name: "membrane bound glycerophospholipid O-acyltransferase 1"
location: "6p22.3"
module: 163
arm: "+"
pooled_cpm: 30.38
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 36
n_dd_up_clean: 5
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/163", "written"]
generated_by: "tahoemap"
---

# MBOAT1

*membrane bound glycerophospholipid O-acyltransferase 1* — 6p22.3

> [!summary] In one line
> MBOAT1 encodes an endoplasmic-reticulum lysophospholipid acyltransferase that re-acylates lyso-phosphatidylethanolamine and lyso-phosphatidylserine, setting the fatty-acid composition of membrane phospholipids.

## What it is

MBOAT1 runs the re-acylation half of the Lands cycle: a phospholipase strips the sn-2 acyl chain from a membrane phospholipid, and a membrane-bound O-acyltransferase puts a new one back. Also called LPEAT1 or LPSAT, it is a multipass ER membrane enzyme preferring lyso-phosphatidylethanolamine and lyso-phosphatidylserine as acceptors and oleoyl-CoA as donor, so its activity shifts membranes toward monounsaturated chains. That specificity gave it a second life in redox biology: MBOAT1 and its paralogue MBOAT2 were identified as ferroptosis suppressors acting independently of GPX4 and FSP1, depleting the polyunsaturated phospholipids that lipid peroxidation requires. In the same work MBOAT1 was reported to be driven transcriptionally by the oestrogen receptor.

## What is uncertain

Nothing establishes MBOAT1 as a direct p53 target: no response element at the locus has been reported, and a repression arm derived from expression behaviour collects genes that fall simply because growth and lipid synthesis fall under arrest. The ferroptosis role rests substantially on gain-of-function overexpression. And since its level tracks oestrogen-receptor status, a hormone-receptor covariate across these pooled lines could generate an association unrelated to p53.

## References

- Hishikawa et al., 2008, PNAS — defined the MBOAT lysophospholipid acyltransferase family, assigning MBOAT1 lyso-PE/lyso-PS acceptor preference.
- Liang et al., 2023, Cell — MBOAT1 and MBOAT2 suppress ferroptosis independently of GPX4 and FSP1, and are induced by oestrogen and androgen receptor respectively.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.56× (z +8.2, q 2e-13, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.319× (z -29.7, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAVER2]] (+0.68, fdr 7e-06), [[ARHGEF26]] (+0.59, fdr 1e-05), [[DLG3]] (+0.56, fdr 2e-05); moves opposite to [[PLAGL1]] (-0.54, fdr 1e-05), [[KCTD11]] (-0.50, fdr 2e-05), [[CLDN14-AS1]] (-0.50, fdr 5e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IGSF3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ANXA11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +8.2 | 2e-13 | 28/45 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 2e-05 | 20/44 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +4.7 | 4e-04 | 14/45 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 0.001 | 13/44 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 10/44 (J82, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.0 | 0.006 | 8/44 (LS 180, LoVo, …) | two highest doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.062 | 8/45 (BT-474, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | 1.39× | +3.2 | 0.10 | 6/45 (C32, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.319×** | -29.7 | 0e+00 | 42/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.252×** | -25.4 | 0e+00 | 41/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.357×** | -18.2 | 0e+00 | 37/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -17.2 | 0e+00 | 36/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.412×** | -16.3 | 0e+00 | 38/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -16.3 | 0e+00 | 37/44 (KATO III, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.478×** | -13.6 | 5e-40 | 32/44 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.496×** | -12.9 | 4e-36 | 31/45 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -12.3 | 3e-33 | 32/44 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -10.4 | 8e-24 | 30/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.568×** | -10.4 | 2e-23 | 31/44 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -9.6 | 3e-20 | 30/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.662×** | -7.0 | 1e-10 | 16/35 (LoVo, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -6.5 | 4e-09 | 24/45 (NCI-H2347, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -6.4 | 6e-09 | 24/44 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -6.2 | 3e-08 | 22/45 (KATO III, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -6.0 | 7e-08 | 25/45 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 77.4 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -28.3) |
| [[KATO III (line)]] | alt | 76.3 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -25.6) |
| [[PANC-1 (line)]] | alt | 72.9 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -30.9) |
| [[SW480 (line)]] | alt | 21.5 | 0 | 13 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 71.0 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.6) |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 39.0 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.5) |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 42.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.2) |
| [[SW48 (line)]] | wt | 31.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -18.0) |
| [[A498 (line)]] | wt | 12.9 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.192× (z -11.8) |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0443× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0894× (z -12.5) |
| [[LS 180 (line)]] | wt | 52.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.1) |
| [[A-427 (line)]] | wt | 22.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.1) |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -10.4) |
| [[A549 (line)]] | wt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.9) |
| [[BT-474 (line)]] | alt | 105 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -12.3) |
| [[C32 (line)]] | wt | 22.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0483× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.3) |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0594× (z -9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.0) |
| [[A-172 (line)]] | wt | 14.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0892× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -8.8) |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.0) |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.8) |
| [[H4 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0970× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 77.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0398× (z -12.0) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -8.6) |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.0) |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAVER2]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ARHGEF26]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DLG3]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RAD54B]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CDC42SE2]] | +0.55 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[DSCC1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CDS1]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 | pathway: Glycerophospholipid biosynthesis; STRING 903 |
| [[HAUS1]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[TANC1]] | +0.53 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[RANBP9]] | +0.53 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[SEMA4D]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAGL1]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[KCTD11]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CLDN14-AS1]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PKD1L1]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ETS1]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[AFF4]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EGFR]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZNF554]] | -0.45 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[PIGL]] | -0.45 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ZNG1A]] | -0.45 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[TNFRSF12A]] | -0.45 | -0.53 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF3]] | B | IGSF3 activity strengthens MBOAT1's drug response | lines that do not express IGSF3 (5) vs lines expressing it (40) | the lines without IGSF3 respond 0.56× as strongly (z diff +2.87); strongest at Panobinostat 0.5 µM: 0.77x vs 0.37x (z diff +5.0) | 0.046 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3; target measured in part of the lines; artifact flags |
| [[ESRP1]] | B | ESRP1 activity raises MBOAT1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without ESRP1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TOP2A]] | B | TOP2A activity raises MBOAT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDS1]] | B | CDS1 activity raises MBOAT1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without CDS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | C | MBOAT1 activity raises ANXA11's level | lines that do not express MBOAT1 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without MBOAT1 | 0.078 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PRKAG2, LY6E-DT, CYB561; maybe low, not absent |

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.6, 37.7); signed map (-18.9, 19.3). **Vector** length 96.4, 24.5% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.3 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | -5.9 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -29.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -16.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -5.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | membrane bound glycerophospholipid O-acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:20,099,684-20,212,469 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC44669, dJ434O11.1, LPEAT1, LPLAT14; previously OACT1 |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family; Lysophospholipid acyltransferases; 1-acylglycerophosphoethanolamine O-acyltransferases |
| Reactome | 5 pathways, smallest: Acyl chain remodelling of PS; Acyl chain remodelling of PE; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNC8](https://www.uniprot.org/uniprotkb/Q6ZNC8) (Membrane-bound glycerophospholipid O-acyltransferase 1):

> Acyltransferase which catalyzes the transfer of an acyl group from an acyl-CoA towards a lysophospholipid producing a phospholipid and participates in the reacylation step of the phospholipid remodeling pathway also known as the Lands cycle. Acts on lysophosphatidylserine (1-acyl-2-hydroxy-sn-glycero-3-phospho-L-serine or LPS) and lysophosphatidylethanolamine (1-acyl-sn-glycero-3-phosphoethanolamine or LPE), and to a lesser extend lysophosphatidylcholine. Prefers oleoyl-CoA as the acyl donor …

**Summary**, from NCBI Gene [154141](https://www.ncbi.nlm.nih.gov/gene/154141):

> This gene belongs to the membrane-bound O-acetyltransferase superfamily. The encoded transmembrane protein is an enzyme that transfers organic compounds, preferably from oleoyl-CoA, to hydroxyl groups of protein targets in membranes. A translocation disrupting this gene may be associated with brachydactyly syndactyly syndrome. Alternately spliced transcript variants have been described for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:21579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21579) · Entrez [154141](https://www.ncbi.nlm.nih.gov/gene/154141) · UniProt [Q6ZNC8](https://www.uniprot.org/uniprotkb/Q6ZNC8) · Ensembl [ENSG00000172197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172197)

## Data

Gene col 10223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10223); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10223]; `tensor/DDL_lfc|DDL_z.npy` [10223]; `embed/gene_vectors.npy` [10223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10223 or target_col == 10223). Every well: [[MBOAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MBOAT1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
