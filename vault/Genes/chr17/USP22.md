---
symbol: "USP22"
type: "gene"
col: 4528
ensembl_id: "ENSG00000124422"
name: "ubiquitin specific peptidase 22"
location: "17p11.2"
module: 153
arm: "+"
pooled_cpm: 123.25
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# USP22

*ubiquitin specific peptidase 22* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.45× (z +8.1, q 4e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -11.7, q 1e-28, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPL]] (+0.66, fdr 1e-05), [[HNRNPK]] (+0.65, fdr 1e-05), [[TUG1]] (+0.64, fdr 4e-05); moves opposite to [[DPM1]] (-0.56, fdr 1e-04), [[CAMLG]] (-0.55, fdr 4e-05), [[RPL18]] (-0.54, fdr 5e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[AFMID]] (-0.54, fdr 1e-04).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +8.1 | 4e-13 | 38/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.7 | 3e-06 | 30/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 3e-05 | 28/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +4.9 | 1e-04 | 26/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 6e-04 | 29/48 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.030 | 19/48 (A498, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.049 | 20/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.085 | 16/48 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.16× | +3.1 | 0.13 | 12/47 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.10× | +3.0 | 0.14 | 11/48 (LoVo, A549, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -11.7 | 1e-28 | 48/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -11.4 | 9e-28 | 47/48 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -9.7 | 8e-20 | 45/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -6.2 | 9e-08 | 31/48 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.770×** | -5.4 | 9e-06 | 29/47 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.851× | -4.9 | 1e-04 | 22/49 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.806×** | -4.6 | 3e-04 | 26/48 (SW 900, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -3.6 | 0.023 | 0/50 | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.863× | -3.2 | 0.099 | 14/48 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 107 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.498× (z -8.8) |
| [[A498 (line)]] | wt | 143 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.98× (z +9.8) | — |
| [[A549 (line)]] | wt | 140 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.22× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 98.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.8) |
| [[LoVo (line)]] | wt | 86.1 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 146 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.510× (z -10.0) |
| [[SW 900 (line)]] | alt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -11.6) |
| [[A-172 (line)]] | wt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 174 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 78.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -10.2) |
| [[HOP62 (line)]] | alt | 206 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.489× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.535× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 78.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 234 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.498× (z -9.9) |
| [[SW480 (line)]] | alt | 142 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.578× (z -9.1) |
| [[A-427 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 109 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.2) |
| [[C32 (line)]] | wt | 118 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -8.7) |
| [[HS-578T (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 110 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.96× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.105× (z -8.7) |
| [[C-33 A (line)]] | alt | 189 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 171 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 127 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | +0.66 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.65 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TUG1]] | +0.64 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ATP13A1]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[WIZ]] | +0.64 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CAPRIN1]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MED12]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[DDX6]] | +0.62 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[STRN4]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[INPPL1]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UBAP2L]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[MTA2]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | -0.56 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[CAMLG]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RPL18]] ⚠ | -0.54 | -0.40 / -0.52 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AFMID]] | -0.54 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PIBF1]] | -0.53 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.52 | -0.24 / -0.54 | both halves | 4e-04 |  |
| [[TMEM191A-1]] | -0.52 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[COMMD6]] | -0.52 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.51 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[EIF4EBP1]] | -0.51 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[RPL36]] | -0.51 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[ATP5MJ]] | -0.50 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises USP22's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, -23.3); signed map (-10.0, -33.6). **Vector** length 101, 26.4% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +6.5 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | -1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.6 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | -0.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -11.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -9.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | +0.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -2.1 | -0.7 |
|  | [[Silodosin (drug)]] 5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:20,999,596-21,043,760 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1063; previously USP3L |
| Gene groups (HGNC) | Ubiquitin specific peptidases; SAGA complex |
| Reactome | 5 pathways, smallest: HATs acetylate histones; Ub-specific processing proteases; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPT9](https://www.uniprot.org/uniprotkb/Q9UPT9) (Ubiquitin carboxyl-terminal hydrolase 22):

> Deubiquitinase that plays a role in several cellular processes including transcriptional regulation, cell cycle progression or innate immunity. As part of the transcription regulatory histone acetylation (HAT) complex SAGA, catalyzes the deubiquitination of both histones H2A and H2B, thereby acting as a transcriptional coactivator. Recruited to specific gene promoters by activators such as MYC, where it is required for transcription. Facilitates cell-cycle progression by stabilizing CCNB1 and …

**Summary**, from NCBI Gene [23326](https://www.ncbi.nlm.nih.gov/gene/23326):

> Enables deubiquitinase activity; enzyme binding activity; and transcription coactivator activity. Contributes to histone H4 acetyltransferase activity. Involved in several processes, including G2/M transition of mitotic cell cycle; protein deubiquitination; and regulation of gene expression. Part of SAGA complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12621) · Entrez [23326](https://www.ncbi.nlm.nih.gov/gene/23326) · UniProt [Q9UPT9](https://www.uniprot.org/uniprotkb/Q9UPT9) · Ensembl [ENSG00000124422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124422)

## Data

Gene col 4528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4528); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4528]; `tensor/DDL_lfc|DDL_z.npy` [4528]; `embed/gene_vectors.npy` [4528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4528 or target_col == 4528). Every well: [[USP22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
