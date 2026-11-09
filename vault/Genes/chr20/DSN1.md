---
symbol: "DSN1"
type: "gene"
col: 7398
ensembl_id: "ENSG00000149636"
name: "DSN1 component of MIS12 kinetochore complex"
location: "20q11.23"
module: 71
arm: "+"
pooled_cpm: 33.23
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DSN1

*DSN1 component of MIS12 kinetochore complex* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.13× (z +6.9, q 3e-09, up in 6 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Cytarabine (drug)]] 0.05 µM: 1.28× (z +3.8, q 0.018, up in 13 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.331× (z -26.2, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPJ]] (+0.78, fdr 7e-06), [[CDCA5]] (+0.75, fdr 7e-06), [[MTBP]] (+0.73, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.9 | 3e-09 | 6/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.37×** | +5.1 | 1e-04 | 23/44 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +4.2 | 0.005 | 20/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +4.1 | 0.006 | 18/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.018 | 13/48 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.021 | 18/47 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.25×** | +3.5 | 0.032 | 16/48 (SNU-423, NCI-H2030, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.23×** | +3.4 | 0.043 | 12/48 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.057 | 8/48 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.15× | +3.3 | 0.057 | 7/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.069 | 9/47 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.14× | +3.1 | 0.085 | 10/48 (HT-29, RKO, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.20×** | +3.1 | 0.085 | 12/48 (A-427, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.331×** | -26.2 | 0e+00 | 38/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.364×** | -16.9 | 0e+00 | 38/47 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -10.7 | 3e-24 | 34/47 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -10.1 | 9e-22 | 35/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -10.0 | 2e-21 | 41/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -9.5 | 2e-19 | 37/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.5 | 2e-19 | 32/48 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -8.6 | 7e-16 | 33/48 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.712×** | -8.0 | 5e-14 | 34/48 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.640×** | -7.5 | 4e-12 | 31/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -7.2 | 3e-11 | 34/47 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -7.2 | 3e-11 | 29/48 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.492×** | -6.1 | 4e-08 | 33/48 (A-427, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -6.0 | 7e-08 | 28/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.698×** | -6.0 | 7e-08 | 26/47 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -5.7 | 3e-07 | 26/48 (KATO III, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0379× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0906× (z -16.3) |
| [[A-427 (line)]] | wt | 43.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0740× (z -21.1) |
| [[Hs 766T (line)]] | wt | 64.3 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.1) |
| [[SW480 (line)]] | alt | 40.0 | 1 (1 ⚠) | 5 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.79× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~38% of this change | [[Digitoxin (drug)]] 0.5 µM 0.258× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 39.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.6) |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -21.2) |
| [[A498 (line)]] | wt | 55.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.1) |
| [[COLO 205 (line)]] | alt | 46.7 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.2) |
| [[H4 (line)]] | wt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -14.5) |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.5) |
| [[A-172 (line)]] | wt | 39.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -12.5) |
| [[HCT15 (line)]] | alt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.3) |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.9) |
| [[KATO III (line)]] | alt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.6) |
| [[SW 1088 (line)]] | alt | 51.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -9.3) |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.8) |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -17.8) |
| [[J82 (line)]] | alt | 69.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -9.6) |
| [[LoVo (line)]] | wt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.7) |
| [[PANC-1 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.53× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~38% of this change | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -12.0) |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.2) |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -11.3) |
| [[SW1417 (line)]] | alt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.1) |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPJ]] | +0.78 | +0.72 / +0.79 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[CDCA5]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[MTBP]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CDT1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[RAD51]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PSMC3IP]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ORC1]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[RFC4]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ATAD5]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SMYD4]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.2, -48.8); signed map (-41.4, -41.3). **Vector** length 116, 33.9% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.2 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +4.2 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.5 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +3.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.6 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -16.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -26.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | DSN1 component of MIS12 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,751,791-36,773,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ469A13.2, MIS13, KNL3, hKNL-3; previously C20orf172 |
| Gene groups (HGNC) | MIS12 kinetochore complex |
| Reactome | 19 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H410](https://www.uniprot.org/uniprotkb/Q9H410) (Kinetochore-associated protein DSN1 homolog):

> Part of the MIS12 complex which is required for normal chromosome alignment and segregation and kinetochore formation during mitosis.

**Summary**, from NCBI Gene [79980](https://www.ncbi.nlm.nih.gov/gene/79980):

> This gene encodes a kinetochore protein that functions as part of the minichromosome instability-12 centromere complex. The encoded protein is required for proper kinetochore assembly and progression through the cell cycle. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:16165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16165) · Entrez [79980](https://www.ncbi.nlm.nih.gov/gene/79980) · UniProt [Q9H410](https://www.uniprot.org/uniprotkb/Q9H410) · Ensembl [ENSG00000149636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149636)

## Data

Gene col 7398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7398); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7398]; `tensor/DDL_lfc|DDL_z.npy` [7398]; `embed/gene_vectors.npy` [7398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7398 or target_col == 7398). Every well: [[DSN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
