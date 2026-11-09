---
symbol: "HEXIM2-AS1"
type: "gene"
col: 13400
ensembl_id: "ENSG00000224505"
name: "HEXIM2 antisense RNA 1"
location: "17q21.31"
module: 23
arm: "+"
pooled_cpm: 12.45
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HEXIM2-AS1

*HEXIM2 antisense RNA 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +7.9, q 2e-12, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.416× (z -8.4, q 2e-14, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.546× (z -5.8, q 9e-07, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BDNF-AS]] (+0.85, fdr 7e-06), [[ANKRD17-DT]] (+0.85, fdr 1e-05), [[CHD1-DT]] (+0.82, fdr 7e-06); moves opposite to [[ARRB2]] (-0.67, fdr 1e-04), [[SIPA1]] (-0.66, fdr 2e-04), [[WASF3]] (-0.66, fdr 3e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.9 | 2e-12 | 33/44 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.1 | 3e-07 | 32/44 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.5 | 0.002 | 20/47 (A498, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.007 | 19/46 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.007 | 24/46 (RKO, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.026 | 16/45 (HCT15, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.96×** | +3.4 | 0.057 | 10/46 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.45×** | +3.3 | 0.077 | 10/48 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.11 | 12/47 (SW480, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.12 | 14/47 (NCI-H23, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.416×** | -8.4 | 2e-14 | 39/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.422×** | -8.3 | 3e-14 | 36/47 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.481×** | -7.0 | 4e-10 | 35/46 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -5.8 | 9e-07 | 33/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -4.8 | 2e-04 | 27/44 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.608×** | -4.8 | 2e-04 | 27/47 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -4.7 | 2e-04 | 25/45 (HT-29, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.615×** | -4.5 | 5e-04 | 22/40 (KATO III, NCI-H460, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -4.3 | 0.001 | 24/43 (A-172, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.443×** | -4.1 | 0.002 | 21/48 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -3.7 | 0.012 | 22/44 (KATO III, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.4 | 0.033 | 18/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.712×** | -3.3 | 0.048 | 16/43 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.713×** | -3.2 | 0.048 | 12/47 (BT-474, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 5.98 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0789× (z -10.5) |
| [[C32 (line)]] | wt | 8.42 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.112× (z -8.6) |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.264× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0808× (z -8.7) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF-AS]] | +0.85 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[ANKRD17-DT]] | +0.85 | +0.86 / +0.57 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.82 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.82 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[ENTPD3-AS1]] | +0.82 | +0.81 / +0.63 | both halves | 7e-06 | same gene group |
| [[AHI1-DT]] | +0.79 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.79 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.78 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.78 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[DNAI4]] | +0.78 | +0.77 / +0.38 | both halves | 6e-05 |  |
| [[PPP1R12A-AS2]] | +0.77 | +0.72 / +0.48 | both halves | 2e-05 | same gene group |
| [[PRANCR]] | +0.77 | +0.74 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | -0.67 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[SIPA1]] | -0.66 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[WASF3]] | -0.66 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[FCHO1]] | -0.65 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CAMK2G]] | -0.65 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MAST3]] | -0.65 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HEXIM2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC13A3]] | B | SLC13A3 activity weakens HEXIM2-AS1's drug response | lines that do not express SLC13A3 (10) vs lines expressing it (38) | the lines without SLC13A3 respond 1.51× as strongly (z diff -0.93); strongest at Panobinostat 0.5 µM: 0.35x vs 0.50x (z diff -1.8) | 0.099 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC01829]] | C | LINC01829 activity raises HEXIM2-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.822). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.5, 17.0); signed map (26.3, -8.4). **Vector** length 99.2, 23.3% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.5 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.0 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.1 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.0 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | HEXIM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:45,150,400-45,161,538 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55857) · Entrez [112268203](https://www.ncbi.nlm.nih.gov/gene/112268203) · Ensembl [ENSG00000224505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224505)

## Data

Gene col 13400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13400); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13400]; `tensor/DDL_lfc|DDL_z.npy` [13400]; `embed/gene_vectors.npy` [13400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13400 or target_col == 13400). Every well: [[HEXIM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEXIM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
