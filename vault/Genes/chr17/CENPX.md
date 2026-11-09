---
symbol: "CENPX"
type: "gene"
col: 9837
ensembl_id: "ENSG00000169689"
name: "centromere protein X"
location: "17q25.3"
module: 58
arm: "+"
pooled_cpm: 15.92
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CENPX

*centromere protein X* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +7.2, q 3e-10, up in 36 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.07× (z +4.4, q 0.001, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -6.8, q 7e-09, down in 34 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.155×, NCI-H2030 0.234×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.138×, RKO 0.107×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM160]] (+0.77, fdr 7e-06), [[NDUFS8]] (+0.75, fdr 7e-06), [[NDUFA3]] (+0.68, fdr 7e-06); moves opposite to [[ZNF610]] (-0.65, fdr 2e-04), [[F8]] (-0.61, fdr 5e-04), [[TRAM2-AS1]] (-0.60, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF655]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.24×** | +7.2 | 3e-10 | 36/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.76×** | +6.2 | 1e-07 | 44/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.71×** | +6.1 | 2e-07 | 43/47 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **2.86×** | +5.5 | 6e-06 | 21/24 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.07×** | +4.4 | 0.001 | 32/47 (HOP62, C32, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.05×** | +4.4 | 0.001 | 34/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.03×** | +4.3 | 0.001 | 30/43 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.52×** | +3.8 | 0.011 | 35/45 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.85×** | +3.7 | 0.011 | 33/45 (NCI-H460, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.92×** | +3.4 | 0.034 | 22/40 (SHP-77, HOP62, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +3.4 | 0.034 | 19/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +3.4 | 0.034 | 28/41 (HCT15, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.27×** | +3.3 | 0.038 | 22/45 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.048 | 26/47 (LoVo, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.97×** | +3.2 | 0.048 | 17/32 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.155×, NCI-H2030 0.234×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.138×, RKO 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -6.8 | 7e-09 | 34/46 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -4.2 | 0.007 | 30/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.616× | -3.0 | 0.47 | 21/47 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.91 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.2) |
| [[RKO (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -8.7) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM160]] | +0.77 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NDUFS8]] | +0.75 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NDUFA3]] | +0.68 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PRELID1]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NHP2]] | +0.65 | +0.55 / +0.41 | both halves | 4e-05 | pathway: Chromosome Maintenance |
| [[AKR7A2]] | +0.65 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.64 | +0.47 / +0.56 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANTKMT]] | +0.64 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[NDUFAB1]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[DCTPP1]] | +0.63 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[AURKAIP1]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PSMB3]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.61 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF610]] | -0.65 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[F8]] | -0.61 | -0.58 / -0.24 | both halves | 5e-04 |  |
| [[TRAM2-AS1]] | -0.60 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[SEPTIN7-DT]] | -0.59 | -0.55 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[LRRC37A3]] | -0.59 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[DDX39B]] | -0.58 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TSGA10]] | -0.58 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.58 | -0.53 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[CTBP1-DT]] | -0.58 | -0.54 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[LEKR1]] | -0.57 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[SRRM2]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ACADM]] | -0.57 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[PAN2]] | -0.56 | -0.61 / -0.21 | both halves | 7e-04 |  |
| [[CGGBP1]] | -0.56 | -0.56 / -0.21 | both halves | 6e-04 |  |
| [[FNBP1P1]] | -0.56 | -0.46 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF655]] | B | ZNF655 activity lowers CENPX's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.81× higher at baseline in the lines without ZNF655 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.7, -19.2); signed map (-37.5, 6.7). **Vector** length 76.3, 22.9% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.51 to 12); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.51 to 12); *Complex I biogenesis* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.6 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.6 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.5 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -2.9 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,018,702-82,024,107 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14480, FAAP10, CENP-X; previously STRA13, MHF2 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 10 pathways, smallest: Fanconi Anemia Pathway; Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MT69](https://www.uniprot.org/uniprotkb/A8MT69) (Centromere protein X):

> DNA-binding component of the Fanconi anemia (FA) core complex. Required for the normal activation of the FA pathway, leading to monoubiquitination of the FANCI-FANCD2 complex in response to DNA damage, cellular resistance to DNA cross-linking drugs, and prevention of chromosomal breakage. In complex with CENPS (MHF heterodimer), crucial cofactor for FANCM in both binding and ATP-dependent remodeling of DNA. Stabilizes FANCM. In complex with CENPS and FANCM (but not other FANC proteins), rapidly …

**Summary**, from NCBI Gene [201254](https://www.ncbi.nlm.nih.gov/gene/201254):

> Enables DNA binding activity. Contributes to double-stranded DNA binding activity. Involved in interstrand cross-link repair; replication fork processing; and resolution of meiotic recombination intermediates. Located in chromatin. Part of FANCM-MHF complex and Fanconi anaemia nuclear complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11422) · Entrez [201254](https://www.ncbi.nlm.nih.gov/gene/201254) · UniProt [A8MT69](https://www.uniprot.org/uniprotkb/A8MT69) · Ensembl [ENSG00000169689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169689)

## Data

Gene col 9837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9837); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9837]; `tensor/DDL_lfc|DDL_z.npy` [9837]; `embed/gene_vectors.npy` [9837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9837 or target_col == 9837). Every well: [[CENPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
