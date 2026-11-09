---
symbol: "LRP1"
type: "gene"
col: 4428
ensembl_id: "ENSG00000123384"
name: "LDL receptor related protein 1"
location: "12q13.3"
module: 99
arm: "+"
pooled_cpm: 146.76
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 46
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# LRP1

*LDL receptor related protein 1* — 12q13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 2.07×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.288× (z -23.1, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.70, fdr 1e-05), [[CDK18]] (+0.66, fdr 1e-05), [[RAB3A]] (+0.65, fdr 1e-05); moves opposite to [[ATR]] (-0.63, fdr 1e-05), [[DPH5-DT]] (-0.63, fdr 1e-05), [[ENOX2]] (-0.62, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EFEMP2]] → it (grade B ⚠); 8 go from it, the strongest it → [[MTMR11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4428.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 2.07×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.24× | +3.3 | 0.27 | 22/47 (HOP62, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.30× | +3.3 | 0.27 | 21/45 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.27 | 24/44 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.288×** | -23.1 | 0e+00 | 44/45 (HT-29, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.172×** | -23.1 | 0e+00 | 44/45 (H4, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.239×** | -17.7 | 0e+00 | 44/45 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.306×** | -15.6 | 0e+00 | 42/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.344×** | -14.0 | 1e-42 | 42/45 (NCI-H1792, H4, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.325×** | -13.9 | 7e-42 | 41/44 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.379×** | -12.7 | 3e-35 | 44/45 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.348×** | -12.6 | 1e-34 | 43/45 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.434×** | -11.0 | 4e-26 | 44/45 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -10.5 | 4e-24 | 38/46 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.451×** | -9.8 | 5e-21 | 39/45 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.482×** | -9.6 | 5e-20 | 39/45 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.471×** | -9.3 | 7e-19 | 33/44 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.524×** | -8.0 | 6e-14 | 35/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.546×** | -7.9 | 7e-14 | 37/45 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.562×** | -7.3 | 8e-12 | 35/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -5.9 | 1e-07 | 32/45 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.3 | 3e-06 | 28/45 (A549, J82, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.682×** | -5.0 | 1e-05 | 30/45 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -5.0 | 1e-05 | 29/45 (LoVo, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -4.7 | 7e-05 | 28/46 (SK-MEL-2, H4, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.699×** | -4.4 | 2e-04 | 30/44 (NCI-H1573, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 21 (12 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0365× (z -23.4) |
| [[NCI-H460 (line)]] | wt | 150 | 0 | 20 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0746× (z -21.3) |
| [[H4 (line)]] | wt | 299 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0340× (z -39.6) |
| [[A549 (line)]] | wt | 449 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -18.4) |
| [[HOP62 (line)]] | alt | 185 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0841× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 207 | 0 | 15 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -14.8) |
| [[HT-29 (line)]] | alt | 221 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0373× (z -43.7) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -20.1) |
| [[J82 (line)]] | alt | 139 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -20.3) |
| [[LoVo (line)]] | wt | 85.9 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0973× (z -19.6) |
| [[SW 900 (line)]] | alt | 72.4 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -22.6) |
| [[SW480 (line)]] | alt | 65.1 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -25.6) |
| [[HCT15 (line)]] | alt | 139 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -24.3) |
| [[RPMI-7951 (line)]] | alt | 435 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -28.6) |
| [[COLO 205 (line)]] | alt | 110 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0256× (z -24.2) |
| [[Hs 766T (line)]] | wt | 348 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0788× (z -34.2) |
| [[LS 180 (line)]] | wt | 52.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 89.0 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -18.8) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -13.6) |
| [[C32 (line)]] | wt | 139 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -29.3) |
| [[SNU-423 (line)]] | alt | 254 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 74.7 | 1 (1 ⚠) | 6 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.07× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.170× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -15.8) |
| [[CHP-212 (line)]] | wt | 187 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.4) |
| [[KATO III (line)]] | alt | 59.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -23.8) |
| [[A498 (line)]] | wt | 227 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -15.0) |
| [[HS-578T (line)]] | alt | 221 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -12.9) |
| [[SW1417 (line)]] | alt | 47.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.8) |
| [[A-172 (line)]] | wt | 704 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -11.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 370 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 42.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.3) |
| [[RKO (line)]] | wt | 61.0 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -14.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.294× (z -8.5) |
| [[A-427 (line)]] | wt | 93.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.9) |
| [[AN3 CA (line)]] | alt | 179 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0828× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 55.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -10.2) |
| [[SW48 (line)]] | wt | 87.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 47.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 225 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 53.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.8) |
| [[SW 1088 (line)]] | alt | 354 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0807× (z -13.7) |
| [[C-33 A (line)]] | alt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.5) |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.109× (z -9.5) |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -10.6) |
| [[SW 1271 (line)]] | alt | 94.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.0) |
| [[BT-474 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 35.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.70 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CDK18]] | +0.66 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 | pathway: Sensory Perception |
| [[NXPH4]] | +0.65 | +0.61 / +0.57 | both halves | 8e-06 | ⚠ **readthrough risk**: NXPH4 lies 3.4 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GPI]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[P4HA2]] | +0.62 | +0.65 / +0.57 | both halves | 9e-06 | same gene group |
| [[CDON]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CLK3]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.61 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PFKFB4]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 | same gene group |
| [[POFUT2]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PLOD1]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RAP1GAP]] | +0.59 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATR]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.63 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.62 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[METTL8]] | -0.58 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[SLC25A13]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 | same gene group |
| [[ITPA]] | -0.57 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[AVEN]] | -0.57 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[SPOPL-DT]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GABPB1]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PRMT3]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | -0.54 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[SPRY3]] | -0.54 | -0.60 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFEMP2]] | B | EFEMP2 activity raises LRP1's level | lines that do not express EFEMP2 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without EFEMP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000198106, ZMIZ1-AS1; maybe low, not absent |
| [[NXPH4]] | B | NXPH4 activity raises LRP1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without NXPH4 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises LRP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KREMEN2]] | B | KREMEN2 activity lowers LRP1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.58× higher at baseline in the lines without KREMEN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTMR11]] | C | LRP1 activity raises MTMR11's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[FGFR1]] | C | LRP1 activity raises FGFR1's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[GNL3L]] | C | LRP1 activity lowers GNL3L's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.36× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[GPATCH4]] | C | LRP1 activity lowers GPATCH4's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.07× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[ITPA]] | C | LRP1 activity lowers ITPA's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.69× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[MRM1]] | C | LRP1 activity lowers MRM1's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.42× higher at baseline in the lines without LRP1 | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent |
| [[KLHL42]] | C | LRP1 activity lowers KLHL42's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.37× higher at baseline in the lines without LRP1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent |
| [[DNAH5]] | C | LRP1 activity lowers DNAH5's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 4.73× higher at baseline in the lines without LRP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -10.5); signed map (-31.0, 21.5). **Vector** length 105, 40.5% of its response variance represented; |z| ≥ 3 in 1,760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.0 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +0.4 |
| fall | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.8 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -12.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -13.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -23.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,128,483-57,213,361 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRP, CD91, LRP1A, APOER, IGFBP3R1, IGFBP-3R; previously APR, A2MR |
| Gene groups (HGNC) | CD molecules; Low density lipoprotein receptors; MicroRNA protein coding host genes |
| Hallmark sets | COAGULATION, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Scavenging of heme from plasma; Retinoid metabolism and transport; Binding and Uptake of Ligands by Scavenger Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07954](https://www.uniprot.org/uniprotkb/Q07954) (Prolow-density lipoprotein receptor-related protein 1):

> Endocytic receptor involved in endocytosis and in phagocytosis of apoptotic cells. Required for early embryonic development (By similarity). Involved in cellular lipid homeostasis. Involved in the plasma clearance of chylomicron remnants and activated LRPAP1 (alpha 2-macroglobulin), as well as the local metabolism of complexes between plasminogen activators and their endogenous inhibitors. Acts as an LRPAP1 alpha-2-macroglobulin receptor. Acts as TAU/MAPT receptor and controls the endocytosis …

**Summary**, from NCBI Gene [4035](https://www.ncbi.nlm.nih.gov/gene/4035):

> This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the encoded protein is necessary for the alpha 2-macroglobulin-mediated clearance of secreted amyloid …

**Accessions** — [HGNC:6692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6692) · Entrez [4035](https://www.ncbi.nlm.nih.gov/gene/4035) · UniProt [Q07954](https://www.uniprot.org/uniprotkb/Q07954) · Ensembl [ENSG00000123384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123384)

## Data

Gene col 4428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4428); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4428]; `tensor/DDL_lfc|DDL_z.npy` [4428]; `embed/gene_vectors.npy` [4428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4428 or target_col == 4428). Every well: [[LRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
