---
symbol: "NMU"
type: "gene"
col: 3039
ensembl_id: "ENSG00000109255"
name: "neuromedin U"
location: "4q12"
module: 67
arm: "+"
pooled_cpm: 9.13
n_lines_expressing: 32
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NMU

*neuromedin U* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.83× (z +8.1, q 4e-13, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.386× (z -9.0, q 2e-16, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCML2]] (+0.65, fdr 1e-05), [[IGFBP2]] (+0.62, fdr 1e-05), [[UGT8]] (+0.60, fdr 1e-05); moves opposite to [[RNF6]] (-0.54, fdr 3e-05), [[ZNF621]] (-0.53, fdr 3e-05), [[LTO1]] (-0.50, fdr 1e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 2 go from it, the strongest it → [[SCML2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +8.1 | 4e-13 | 16/30 (NCI-H2347, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.13×** | +7.2 | 2e-10 | 13/25 (A-172, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +5.9 | 5e-07 | 17/28 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.34×** | +4.2 | 0.003 | 10/26 (J82, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.45×** | +3.5 | 0.049 | 11/28 (AN3 CA, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.28×** | +3.4 | 0.069 | 10/30 (LoVo, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.092 | 7/29 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | 1.41× | +3.1 | 0.12 | 6/16 (J82, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.1 | 0.12 | 10/24 (HCT15, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.37× | +3.0 | 0.15 | 8/29 (J82, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.386×** | -9.0 | 2e-16 | 22/26 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.581×** | -7.2 | 2e-10 | 19/28 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -6.0 | 3e-07 | 20/29 (COLO 205, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -4.6 | 7e-04 | 17/29 (H4, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.622×** | -4.5 | 9e-04 | 14/28 (LS 180, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.626×** | -4.4 | 1e-03 | 15/29 (LS 180, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -4.3 | 0.001 | 15/29 (LOX-IMVI, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.698×** | -3.4 | 0.052 | 15/28 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.515×** | -3.3 | 0.067 | 7/30 (LS 180, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.694×** | -3.2 | 0.067 | 7/30 (CHP-212, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 30.3 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0252× (z -19.4) |
| [[LS 180 (line)]] | wt | 49.9 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.7) |
| [[COLO 205 (line)]] | alt | 43.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0118× (z -17.1) |
| [[A-427 (line)]] | wt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.5) |
| [[KATO III (line)]] | alt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -8.9) |
| [[LoVo (line)]] | wt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0675× (z -13.9) |
| [[A-172 (line)]] | wt | 7.43 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.191× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0662× (z -9.6) |
| [[RKO (line)]] | wt | 7.44 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0755× (z -9.6) |
| [[A498 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCML2]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[IGFBP2]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[UGT8]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[GPSM2]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 | pathway: G alpha (i) signalling events; STRING 465 |
| [[A2MP1]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[UBE2T]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[STIL]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[CENPW]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MIS18BP1]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[DEPDC1B]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PTTG1]] | +0.55 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[KIF18B]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LTO1]] | -0.50 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[EXOC7]] | -0.50 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[EIF5]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PARP3]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[AP5B1]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[DESI1]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DVL3]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[FLII]] | -0.47 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[UEVLD]] | -0.47 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NMU's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCML2]] | B | NMU activity lowers SCML2's level | lines that do not express NMU (18) vs lines expressing it (32) | 2.02× higher at baseline in the lines without NMU | 0.088 | ⚠ within organs, on part of the lines; also absent: S100A2, ANK3, FAM83F; maybe low, not absent |
| [[ILDR2]] | B | NMU activity raises ILDR2's level | lines that do not express NMU (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without NMU | 0.099 | ⚠ within organs, on part of the lines; also absent: S100A2, ANK3, FAM83F; maybe low, not absent |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-31.3, -55.3); signed map (-49.8, -37.7). **Vector** length 66.9, 15.5% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.51 to 4); *Nucleosome assembly* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.9 | +7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +3.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | -0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -9.0 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | neuromedin U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:55,595,229-55,636,698 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuropeptides |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 7 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P48645](https://www.uniprot.org/uniprotkb/P48645) (Neuromedin-U):

> [Neuromedin-U-25]: Multifunctional neuropeptide that acts via two G protein-coupled receptors, NMUR1 and NMUR2. Functionally, is involved in pleiotropic roles, including regulation of feeding, energy balance, blood pressure and smooth muscle contraction (By similarity). Additionally modulates hormone release and inflammatory responses in a tissue- and receptor-dependent manner. Mechanistically, binding to NMUR1 or NMUR2 results in coupling of receptors to Galpha proteins, namely GNAQ/Gaq or …

**Summary**, from NCBI Gene [10874](https://www.ncbi.nlm.nih.gov/gene/10874):

> This gene encodes a member of the neuromedin family of neuropeptides. The encoded protein is a precursor that is proteolytically processed to generate a biologically active neuropeptide that plays a role in pain, stress, immune-mediated inflammatory diseases and feeding regulation. Increased expression of this gene was observed in renal, pancreatic and lung cancers. Alternative splicing results in multiple transcript variants encoding different isoforms. Some of these isoforms may undergo …

**Accessions** — [HGNC:7859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7859) · Entrez [10874](https://www.ncbi.nlm.nih.gov/gene/10874) · UniProt [P48645](https://www.uniprot.org/uniprotkb/P48645) · Ensembl [ENSG00000109255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109255)

## Data

Gene col 3039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3039); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3039]; `tensor/DDL_lfc|DDL_z.npy` [3039]; `embed/gene_vectors.npy` [3039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3039 or target_col == 3039). Every well: [[NMU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
