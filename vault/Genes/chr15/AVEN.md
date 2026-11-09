---
symbol: "AVEN"
type: "gene"
col: 9861
ensembl_id: "ENSG00000169857"
name: "apoptosis and caspase activation inhibitor"
location: "15q14"
module: 124
arm: "+"
pooled_cpm: 23.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# AVEN

*apoptosis and caspase activation inhibitor* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.63× (z +8.0, q 7e-13, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.384× (z -11.1, q 1e-25, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSB]] (+0.77, fdr 7e-06), [[CRPPA]] (+0.77, fdr 7e-06), [[DPH5-DT]] (+0.76, fdr 1e-05); moves opposite to [[RAB3A]] (-0.75, fdr 1e-05), [[PLEKHH3]] (-0.73, fdr 7e-06), [[KBTBD3]] (-0.73, fdr 1e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.0 | 7e-13 | 42/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.3 | 9e-11 | 32/41 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +7.0 | 4e-10 | 32/46 (LS 180, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.6 | 4e-09 | 21/32 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.3 | 3e-08 | 27/46 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 1e-05 | 26/46 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.1 | 3e-05 | 30/46 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.6 | 3e-04 | 22/37 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.4 | 6e-04 | 27/46 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 8e-04 | 25/47 (COLO 205, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +4.2 | 0.002 | 23/47 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +3.9 | 0.004 | 24/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +3.5 | 0.020 | 17/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.020 | 17/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +3.4 | 0.026 | 11/48 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.050 | 19/47 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.384×** | -11.1 | 1e-25 | 42/48 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.409×** | -10.3 | 1e-22 | 39/48 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -10.3 | 1e-22 | 40/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.434×** | -9.7 | 6e-20 | 40/45 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -6.9 | 5e-10 | 33/48 (J82, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.686×** | -6.2 | 6e-08 | 34/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.368×** | -6.0 | 1e-07 | 35/48 (MIA PaCa-2, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.649×** | -5.0 | 4e-05 | 29/46 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -4.9 | 7e-05 | 27/48 (RPMI-7951, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.729×** | -3.7 | 0.013 | 18/47 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | 0.768× | -3.1 | 0.11 | 20/44 (SW1417, COLO 205, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.8) |
| [[A498 (line)]] | wt | 27.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.258× (z -9.1) |
| [[HOP62 (line)]] | alt | 24.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +9.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.226× (z -10.0) |
| [[J82 (line)]] | alt | 28.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -9.6) |
| [[LoVo (line)]] | wt | 38.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +10.0) | [[Panobinostat (drug)]] 0.05 µM 0.280× (z -9.4) |
| [[KATO III (line)]] | alt | 24.3 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.230× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.241× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.252× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.6) |
| [[RKO (line)]] | wt | 24.2 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.181× (z -10.5) |
| [[SNU-1 (line)]] | wt | 37.1 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0383× (z -16.6) |
| [[A-172 (line)]] | wt | 22.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -8.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.119× (z -9.5) |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.295× (z -9.5) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0928× (z -10.3) |
| [[SW480 (line)]] | alt | 39.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.298× (z -10.7) |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSB]] | +0.77 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CRPPA]] | +0.77 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.76 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[SPRY3]] | +0.74 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ATXN10]] | +0.74 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PCBD2]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[EFCAB2]] | +0.73 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | +0.73 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.72 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[ZNF124]] | +0.72 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[EPM2A]] | +0.72 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ITPA]] | +0.71 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.75 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.73 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.73 | -0.55 / -0.76 | both halves | 1e-05 |  |
| [[ARL3]] | -0.71 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[SNAPC3]] | -0.71 | -0.73 / -0.42 | both halves | 4e-05 |  |
| [[GPR160]] | -0.71 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[ALAD]] | -0.70 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.69 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CFD]] | -0.69 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ARL6]] | -0.67 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PDK3]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[PJA2]] | -0.67 | -0.67 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AVEN's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AVEN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.5, -8.2); signed map (22.8, -28.2). **Vector** length 128, 35.5% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.9 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.7 | -9.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.7 | -11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -10.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.2 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -2.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis and caspase activation inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:33,858,782-34,075,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDCD12 |
| Reactome | 7 pathways, smallest: Formation of apoptosome; Regulation of the apoptosome activity; Cytochrome c-mediated apoptotic response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQS1](https://www.uniprot.org/uniprotkb/Q9NQS1) (Cell death regulator Aven):

> Protects against apoptosis mediated by Apaf-1.

**Summary**, from NCBI Gene [57099](https://www.ncbi.nlm.nih.gov/gene/57099):

> Involved in negative regulation of apoptotic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13509) · Entrez [57099](https://www.ncbi.nlm.nih.gov/gene/57099) · UniProt [Q9NQS1](https://www.uniprot.org/uniprotkb/Q9NQS1) · Ensembl [ENSG00000169857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169857)

## Data

Gene col 9861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9861); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9861]; `tensor/DDL_lfc|DDL_z.npy` [9861]; `embed/gene_vectors.npy` [9861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9861 or target_col == 9861). Every well: [[AVEN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AVEN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
