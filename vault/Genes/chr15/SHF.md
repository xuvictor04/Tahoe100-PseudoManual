---
symbol: "SHF"
type: "gene"
col: 6192
ensembl_id: "ENSG00000138606"
name: "Src homology 2 domain containing F"
location: "15q21.1"
module: 161
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# SHF

*Src homology 2 domain containing F* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.62× (z +17.5, q 0e+00, up in 17 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +11.3, q 1e-27, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.542× (z -6.8, q 8e-09, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK3]] (+0.70, fdr 7e-06), [[ASMTL]] (+0.67, fdr 7e-06), [[FCHO1]] (+0.64, fdr 1e-05); moves opposite to [[UBE3B]] (-0.57, fdr 3e-05), [[TAOK1]] (-0.57, fdr 2e-05), [[PARG]] (-0.55, fdr 2e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.62×** | +17.5 | 0e+00 | 17/20 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +15.3 | 0e+00 | 8/10 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +12.2 | 9e-32 | 8/10 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +11.3 | 1e-27 | 32/41 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +8.4 | 7e-15 | 25/36 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +5.8 | 6e-07 | 17/39 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +5.4 | 5e-06 | 14/41 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.043 | 8/36 (A-172, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.063 | 10/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.087 | 8/39 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.087 | 7/38 (SW48, HT-29, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.095 | 5/34 (H4, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -6.8 | 8e-09 | 21/31 (CFPAC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -6.7 | 8e-09 | 17/27 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -4.3 | 0.003 | 13/37 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.698×** | -4.1 | 0.005 | 11/41 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -4.0 | 0.007 | 17/34 (CFPAC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -3.8 | 0.014 | 12/40 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.729×** | -3.6 | 0.021 | 10/37 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -3.3 | 0.063 | 14/33 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.069 | 4/42 (A-427, SW480, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.069 | 2/42 (NCI-H460, NCI-H661) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.741×** | -3.2 | 0.069 | 5/38 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.069 | 2/39 (RPMI-7951, AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.8 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.7) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.0415× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -8.7) |
| [[COLO 205 (line)]] | alt | 32.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0388× (z -17.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.0) |
| [[A498 (line)]] | wt | 2.56 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0581× (z -9.6) |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 1 | — | [[Regorafenib (drug)]] 0.05 µM 0.0719× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 8.78 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0929× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK3]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ASMTL]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[FCHO1]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CADM4]] | +0.63 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SGSM1]] | +0.62 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[SUSD4]] | +0.61 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[SYP]] | +0.61 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[SEMA6B]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ATP2A3]] | +0.60 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[BAIAP3]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ATP1A3]] | +0.60 | +0.24 / +0.64 | both halves | 4e-04 |  |
| [[SEMA3F]] | +0.59 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE3B]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TAOK1]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PARG]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[DHRS4-AS1]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PALB2]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ITFG1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[GSTCD]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PUS10]] | -0.52 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[ANGEL2]] | -0.51 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[UBTF]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TDRD3]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[PPP1R8]] | -0.51 | -0.37 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SHF's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SHF's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises SHF's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.9, 1.1); signed map (-22.1, 28.9). **Vector** length 60.0, 9.67% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Src homology 2 domain containing F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,167,214-45,201,175 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7M4L6](https://www.uniprot.org/uniprotkb/Q7M4L6) (SH2 domain-containing adapter protein F):

> Adapter protein which may play a role in the regulation of apoptosis in response to PDGF.

**Summary**, from NCBI Gene [90525](https://www.ncbi.nlm.nih.gov/gene/90525):

> Predicted to enable phosphotyrosine residue binding activity. Predicted to be involved in apoptotic process and signal transduction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25116) · Entrez [90525](https://www.ncbi.nlm.nih.gov/gene/90525) · UniProt [Q7M4L6](https://www.uniprot.org/uniprotkb/Q7M4L6) · Ensembl [ENSG00000138606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138606)

## Data

Gene col 6192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6192); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6192]; `tensor/DDL_lfc|DDL_z.npy` [6192]; `embed/gene_vectors.npy` [6192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6192 or target_col == 6192). Every well: [[SHF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
