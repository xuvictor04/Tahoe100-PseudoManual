---
symbol: "TRIM8"
type: "gene"
col: 10072
ensembl_id: "ENSG00000171206"
name: "tripartite motif containing 8"
location: "10q24.32"
module: 173
arm: "+"
pooled_cpm: 19.83
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 34
n_dd_up_clean: 9
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# TRIM8

*tripartite motif containing 8* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.2, q 3e-10, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.275× (z -20.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45]] (+0.70, fdr 3e-05), [[MMRN2]] (+0.68, fdr 2e-05), [[CHMP4B]] (+0.62, fdr 1e-05); moves opposite to [[NBAS]] (-0.59, fdr 1e-04), [[INTS10]] (-0.59, fdr 1e-05), [[UBE2Q2P2]] (-0.57, fdr 3e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.2 | 3e-10 | 27/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.48×** | +6.3 | 1e-07 | 29/48 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 4e-07 | 24/48 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.5 | 0.001 | 22/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +4.4 | 0.001 | 19/48 (SW1417, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.004 | 13/47 (SW480, SW48, …) | two highest doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.006 | 12/45 (NCI-H1792, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.008 | 17/47 (SW1417, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.8 | 0.010 | 13/38 (SHP-77, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.010 | 10/46 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +3.7 | 0.010 | 12/47 (SHP-77, LoVo, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.031 | 11/46 (HCT15, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.21×** | +3.1 | 0.094 | 13/42 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.275×** | -20.3 | 0e+00 | 46/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.290×** | -19.5 | 0e+00 | 45/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.323×** | -17.8 | 0e+00 | 43/47 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.409×** | -14.1 | 8e-43 | 44/47 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -9.8 | 2e-20 | 35/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -8.5 | 2e-15 | 30/47 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.589×** | -8.3 | 7e-15 | 35/47 (SW480, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.370×** | -8.2 | 2e-14 | 38/46 (A498, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.705×** | -7.8 | 5e-13 | 29/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.391×** | -7.7 | 6e-13 | 36/47 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.412×** | -7.3 | 2e-11 | 33/45 (AsPC-1, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.413×** | -7.3 | 2e-11 | 30/44 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.640×** | -7.0 | 9e-11 | 27/47 (SW48, HT-29, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -6.3 | 1e-08 | 28/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.468×** | -6.2 | 2e-08 | 28/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.503×** | -5.6 | 6e-07 | 31/43 (A498, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 25.1 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.168× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 39.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 13.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.194× (z -11.6) |
| [[SW480 (line)]] | alt | 21.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -17.8) |
| [[A498 (line)]] | wt | 23.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -10.0) |
| [[A549 (line)]] | wt | 20.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -10.3) |
| [[HOP62 (line)]] | alt | 19.3 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -10.0) |
| [[LoVo (line)]] | wt | 14.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.253× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -15.5) |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -11.9) |
| [[SW48 (line)]] | wt | 24.9 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.128× (z -9.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.128× (z -9.7) |
| [[A-427 (line)]] | wt | 14.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.189× (z -10.4) |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 51.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -13.3) |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -11.8) |
| [[KATO III (line)]] | alt | 12.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0735× (z -15.5) |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -11.2) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -8.9) |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.257× (z -10.1) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -9.4) |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0943× (z -8.7) |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.168× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -9.2) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -9.6) |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -12.5) |
| [[RKO (line)]] | wt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0908× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.166× (z -8.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.8) |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45]] | +0.70 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.68 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CHMP4B]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SIX5]] | +0.61 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[ZNF641]] | +0.60 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[STK11]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ENO3]] | +0.59 | +0.62 / +0.32 | both halves | 2e-04 |  |
| [[KHNYN]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[RGL2]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PIK3IP1-DT]] | +0.59 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[MEPCE]] | +0.59 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[TAB3]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBAS]] | -0.59 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[INTS10]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UBE2Q2P2]] | -0.57 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[RNF216]] | -0.57 | -0.42 / -0.46 | both halves | 4e-05 | same gene group |
| [[IMMT]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[OPA1]] | -0.52 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[CAMK2G]] | -0.52 | -0.36 / -0.44 | both halves | 1e-04 | pathway: Interferon Signaling |
| [[EPS15L1]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HACE1]] | -0.52 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[NME2]] | -0.51 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[KPNB1]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 | pathway: Interferon Signaling |
| [[PPP1R12B]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.8, 9.2); signed map (19.3, -8.4). **Vector** length 104, 25.3% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +7.0 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -14.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.4 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -9.8 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -7.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,642,503-102,658,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GERP; previously RNF27 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZR9](https://www.uniprot.org/uniprotkb/Q9BZR9) (E3 ubiquitin-protein ligase TRIM8):

> E3 ubiquitin-protein ligase that participates in multiple biological processes including cell survival, differentiation, apoptosis, and in particular, the innate immune response. Participates in the activation of interferon-gamma signaling by promoting proteasomal degradation of the repressor SOCS1. Plays a positive role in the TNFalpha and IL-1beta signaling pathways. Mechanistically, induces the 'Lys-63'-linked polyubiquitination of MAP3K7/TAK1 component leading to the activation of …

**Summary**, from NCBI Gene [81603](https://www.ncbi.nlm.nih.gov/gene/81603):

> This gene encodes a member of the tripartite motif (TRIM) protein family. Based on similarities to other proteins, the encoded protein is suspected to be an E3 ubiquitin-protein ligase. Regulation of this gene may be altered in some cancers. Mutations resulting in a truncated protein product have been observed in early-onset epileptic encephalopathy (EOEE). [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:15579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15579) · Entrez [81603](https://www.ncbi.nlm.nih.gov/gene/81603) · UniProt [Q9BZR9](https://www.uniprot.org/uniprotkb/Q9BZR9) · Ensembl [ENSG00000171206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171206)

## Data

Gene col 10072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10072); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10072]; `tensor/DDL_lfc|DDL_z.npy` [10072]; `embed/gene_vectors.npy` [10072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10072 or target_col == 10072). Every well: [[TRIM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
