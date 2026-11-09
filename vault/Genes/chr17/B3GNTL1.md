---
symbol: "B3GNTL1"
type: "gene"
col: 10641
ensembl_id: "ENSG00000175711"
name: "queuosine-tRNA galactosyltransferase"
location: "17q25.3"
module: 1
arm: "+"
pooled_cpm: 30.27
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# B3GNTL1

*queuosine-tRNA galactosyltransferase* — 17q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 3.64×; ⚠ cell-cycle shift, explains ~37% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.505× (z -15.9, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF121]] (+0.60, fdr 1e-05), [[CEP83]] (+0.59, fdr 3e-05), [[CASC19]] (+0.59, fdr 1e-05); moves opposite to [[RRAGC]] (-0.57, fdr 1e-05), [[NRBP1]] (-0.57, fdr 4e-05), [[CERT1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 3.64×; ⚠ cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.23× | +3.4 | 0.42 | 13/45 (A498, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.42 | 18/46 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -15.9 | 0e+00 | 39/47 (COLO 205, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.651×** | -10.0 | 6e-21 | 24/46 (NCI-H23, CHP-212, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -8.1 | 1e-13 | 28/46 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -6.9 | 7e-10 | 27/46 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.715×** | -6.4 | 1e-08 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -6.4 | 1e-08 | 27/47 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.696×** | -6.0 | 2e-07 | 25/46 (PANC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.698×** | -5.7 | 1e-06 | 22/45 (A-427, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.681×** | -5.5 | 2e-06 | 21/43 (A-427, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -5.5 | 2e-06 | 26/46 (NCI-H23, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.715×** | -5.3 | 6e-06 | 21/46 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -5.2 | 1e-05 | 24/44 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.701×** | -5.1 | 2e-05 | 23/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.743×** | -4.9 | 5e-05 | 23/46 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.744×** | -4.8 | 5e-05 | 22/47 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.737×** | -4.8 | 5e-05 | 21/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.765×** | -4.7 | 1e-04 | 22/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -4.6 | 1e-04 | 21/45 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.780×** | -4.5 | 2e-04 | 17/47 (SW480, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.806×** | -4.4 | 3e-04 | 17/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.6 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -13.4) |
| [[HOP62 (line)]] | alt | 41.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -13.5) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 83.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.239× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 85.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -24.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -15.3) |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.4) |
| [[SW480 (line)]] | alt | 41.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.0) |
| [[A498 (line)]] | wt | 36.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.2) |
| [[J82 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.4) |
| [[A549 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -8.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.8) |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0360× (z -16.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -21.0) |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 8.20 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.114× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -13.1) |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF121]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CEP83]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CASC19]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SEH1L]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[WDR4]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[COA1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PALD1]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.55 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[SNRPD1]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[BCAN-AS2]] | +0.54 | +0.43 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NRBP1]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CERT1]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RC3H1]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[OPTN]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[DCAF5]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SECISBP2L]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[BMPR2]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[GABARAP]] ⚠ | -0.51 | -0.48 / -0.58 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NPEPPS]] | -0.50 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[TAX1BP1]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[VAMP8]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.5, -44.1); signed map (-3.4, -50.5). **Vector** length 93.6, 20.3% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -15.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | queuosine-tRNA galactosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,942,149-83,051,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B3GNT8; previously B3GNTL1 |
| Gene groups (HGNC) | Glycosyltransferase family 2 |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q67FW5](https://www.uniprot.org/uniprotkb/Q67FW5) (Queuosine-tRNA galactosyltransferase):

> Glycosyltransferase that specifically catalyzes galactosylation of cytoplasmic tRNA(Tyr) modified with queuosine at position 34 (queuosine(34)). Galactosylates the cyclopentene hydroxyl group of queuosine(34) in tRNA(Tyr) to form galactosyl-queuosine(34). Mannosylation of queuosine(34) in tRNA(Tyr) is required to slow-down elongation at cognate codons UAC and suppress stop codon readthrough, thereby regulating protein translation.

**Summary**, from NCBI Gene [146712](https://www.ncbi.nlm.nih.gov/gene/146712):

> Enables tRNA-queuosine(34) galactosyltransferase activity. Involved in regulation of translation and tRNA wobble guanine modification. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21727) · Entrez [146712](https://www.ncbi.nlm.nih.gov/gene/146712) · UniProt [Q67FW5](https://www.uniprot.org/uniprotkb/Q67FW5) · Ensembl [ENSG00000175711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175711)

## Data

Gene col 10641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10641); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10641]; `tensor/DDL_lfc|DDL_z.npy` [10641]; `embed/gene_vectors.npy` [10641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10641 or target_col == 10641). Every well: [[B3GNTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
