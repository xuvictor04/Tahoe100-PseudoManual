---
symbol: "ATP2A2"
type: "gene"
col: 10491
ensembl_id: "ENSG00000174437"
name: "ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2"
location: "12q24.11"
module: 20
arm: "+"
pooled_cpm: 194.15
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ATP2A2

*ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.64× (z +9.0, q 9e-17, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.735× (z -5.6, q 1e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.68, fdr 7e-06), [[UGGT1]] (+0.66, fdr 1e-05), [[CMPK1]] (+0.64, fdr 7e-06); moves opposite to [[MRPS31]] (-0.67, fdr 7e-06), [[RP9]] (-0.64, fdr 7e-06), [[NAA30]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +9.0 | 9e-17 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 1e-14 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +7.6 | 5e-12 | 41/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.1 | 2e-10 | 37/48 (HCT15, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +7.0 | 3e-10 | 42/49 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.2 | 4e-08 | 35/47 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 5e-07 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.5 | 3e-06 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 3e-05 | 34/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.8 | 8e-05 | 33/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.6 | 2e-04 | 30/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.005 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.15× | +3.6 | 0.012 | 6/49 (A-427, SNU-423, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.035 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 1.13× | +3.0 | 0.093 | 5/48 (HOP62, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -5.6 | 1e-05 | 34/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -5.4 | 2e-05 | 32/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -5.1 | 5e-05 | 36/47 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.776×** | -4.6 | 5e-04 | 30/48 (J82, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.1 | 0.005 | 30/48 (A-172, A-427, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.802×** | -4.0 | 0.005 | 25/48 (LS 180, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.803×** | -4.0 | 0.005 | 26/48 (A-427, A-172, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -3.9 | 0.006 | 25/49 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.809×** | -3.9 | 0.006 | 28/48 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -3.8 | 0.007 | 15/48 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.813×** | -3.8 | 0.007 | 26/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.8 | 0.008 | 19/48 (RKO, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.6 | 0.012 | 19/48 (RKO, LS 180, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.025 | 25/49 (HepG2/C3A, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.028 | 20/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.886× | -3.2 | 0.056 | 6/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 155 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 174 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +14.6) | — |
| [[A-172 (line)]] | wt | 134 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.389× (z -11.9) |
| [[PANC-1 (line)]] | alt | 183 | 3 | 1 | [[PH-797804 (drug)]] 5 µM 4.46× (z +10.4) | [[Harringtonine (drug)]] 0.5 µM 0.524× (z -8.6) |
| [[SW48 (line)]] | wt | 224 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +11.2) | — |
| [[A-427 (line)]] | wt | 201 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -20.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.470× (z -8.8) |
| [[A549 (line)]] | wt | 219 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | — |
| [[KATO III (line)]] | alt | 234 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 169 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.23× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 222 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.497× (z -9.5) |
| [[SW1417 (line)]] | alt | 161 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.0) | — |
| [[A498 (line)]] | wt | 191 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 262 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 163 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 176 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 240 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[J82 (line)]] | alt | 259 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 244 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.472× (z -9.5) |
| [[LS 180 (line)]] | wt | 225 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.4) | — |
| [[RKO (line)]] | wt | 304 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -11.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 162 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +9.2) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 175 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 162 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 229 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.68 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.66 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[CMPK1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.63 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RPN1]] | +0.62 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CHID1]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[BANF1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[STT3B]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[MACROH2A1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[VCP]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 | STRING 416 |

## Genes that move opposite

*53 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31]] | -0.67 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[RP9]] | -0.64 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[NAA30]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[SMIM29]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[LACTB]] | -0.62 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[ZNF397]] | -0.62 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[COMMD3]] | -0.62 | -0.57 / -0.64 | both halves | 8e-06 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.54 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDRG1]] | -0.60 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[PIM3]] | -0.59 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RRAGC]] | -0.59 | -0.54 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.2, -9.2); signed map (-24.1, -40.3). **Vector** length 131, 43.9% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +9.5 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | +9.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -7.3 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,280,756-110,351,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SERCA2; previously ATP2B, DAR |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Hallmark sets | INFLAMMATORY_RESPONSE, XENOBIOTIC_METABOLISM, MTORC1_SIGNALING |
| Reactome | 15 pathways, smallest: Reduction of cytosolic Ca++ levels; Pre-NOTCH Processing in Golgi; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P16615](https://www.uniprot.org/uniprotkb/P16615) (Sarcoplasmic/endoplasmic reticulum calcium ATPase 2):

> This magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen. Involved in autophagy in response to starvation. Upon interaction with VMP1 and activation, controls ER-isolation membrane contacts for autophagosome formation. Also modulates ER contacts with lipid droplets, mitochondria and endosomes. In coordination with FLVCR2 mediates heme-stimulated switching from mitochondrial ATP synthesis to …

**Summary**, from NCBI Gene [488](https://www.ncbi.nlm.nih.gov/gene/488):

> This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darier-White disease, also known as keratosis follicularis, an autosomal dominant skin disorder …

**Accessions** — [HGNC:812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:812) · Entrez [488](https://www.ncbi.nlm.nih.gov/gene/488) · UniProt [P16615](https://www.uniprot.org/uniprotkb/P16615) · Ensembl [ENSG00000174437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174437)

## Data

Gene col 10491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10491); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10491]; `tensor/DDL_lfc|DDL_z.npy` [10491]; `embed/gene_vectors.npy` [10491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10491 or target_col == 10491). Every well: [[ATP2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
