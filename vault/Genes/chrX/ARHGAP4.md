---
symbol: "ARHGAP4"
type: "gene"
col: 1601
ensembl_id: "ENSG00000089820"
name: "Rho GTPase activating protein 4"
location: "Xq28"
module: 18
arm: "+"
pooled_cpm: 15.56
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ARHGAP4

*Rho GTPase activating protein 4* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.17× (z +16.5, q 0e+00, up in 17 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.47× (z +5.7, q 6e-07, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.779× (z -5.2, q 9e-05, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.72, fdr 1e-05), [[RPSA]] (+0.70, fdr 7e-06), [[AKT1]] (+0.70, fdr 7e-06); moves opposite to [[SUMO4]] (-0.68, fdr 1e-05), [[DCP1A]] (-0.66, fdr 1e-05), [[PIGBOS1]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[YBX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +16.5 | 0e+00 | 17/18 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.83×** | +15.5 | 0e+00 | 31/38 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.51×** | +13.7 | 3e-40 | 36/46 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.33×** | +12.6 | 2e-34 | 32/46 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +11.9 | 2e-30 | 23/26 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.20×** | +11.8 | 6e-30 | 35/46 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.42×** | +7.4 | 8e-12 | 22/44 (A549, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.65×** | +7.1 | 7e-11 | 19/38 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.7 | 6e-07 | 16/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.4 | 5e-06 | 19/46 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.2 | 1e-05 | 17/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.4 | 4e-04 | 9/46 (NCI-H1792, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.34×** | +4.2 | 0.001 | 13/40 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.28×** | +3.6 | 0.013 | 12/45 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[γ-Oryzanol (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.024 | 6/45 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.065 | 10/46 (Panc 03.27, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -5.2 | 9e-05 | 18/46 (AsPC-1, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.560×** | -4.5 | 0.002 | 14/41 (NCI-H1792, AN3 CA, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 0.002 | 14/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **0.741×** | -4.1 | 0.005 | 13/42 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.006 | 15/44 (SW48, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.781×** | -3.7 | 0.023 | 9/46 (SW48, NCI-H661, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.805×** | -3.4 | 0.055 | 9/47 (SW480, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.802×** | -3.3 | 0.074 | 10/44 (SNU-1, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.811× | -3.1 | 0.11 | 12/43 (PANC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.7 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -10.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 21.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.70× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 18.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 6.52 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0589× (z -9.9) |
| [[HS-578T (line)]] | alt | 5.39 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.109× (z -8.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0805× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 7.56 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0834× (z -9.2) |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[RPSA]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[AKT1]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCAR2]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[POLD1]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[TFDP1]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[CHID1]] | +0.66 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RNPS1]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MAT2A]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO4]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.66 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.66 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[RAB9A]] | -0.65 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[NKAP]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[EAPP]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[FDX2]] | -0.64 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RRAGC]] | -0.64 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ASB8]] | -0.64 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[SCAND1]] | -0.64 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CIR1]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.63 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises ARHGAP4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without YBX2 | 0.003 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-20.9, -26.5); signed map (-24.7, -42.9). **Vector** length 73.9, 12.1% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +7.4 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +11.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.8 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.3 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.1 | -1.8 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,907,367-153,934,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0131, C1, p115, RhoGAP4, SrGAP4 |
| Gene groups (HGNC) | F-BAR domain containing; AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P98171](https://www.uniprot.org/uniprotkb/P98171) (Rho GTPase-activating protein 4):

> Inhibitory effect on stress fiber organization. May down-regulate Rho-like GTPase in hematopoietic cells.

**Summary**, from NCBI Gene [393](https://www.ncbi.nlm.nih.gov/gene/393):

> This gene encodes a member of the rhoGAP family of proteins which play a role in the regulation of small GTP-binding proteins belonging to the RAS superfamily. The protein encoded by the orthologous gene in rat is localized to the Golgi complex and can redistribute to microtubules. The rat protein stimulates the activity of some Rho GTPases in vitro. Genomic deletions of this gene and a neighboring gene have been found in patients with nephrogenic diabetes insipidus. Multiple transcript …

**Accessions** — [HGNC:674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:674) · Entrez [393](https://www.ncbi.nlm.nih.gov/gene/393) · UniProt [P98171](https://www.uniprot.org/uniprotkb/P98171) · Ensembl [ENSG00000089820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089820)

## Data

Gene col 1601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1601); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1601]; `tensor/DDL_lfc|DDL_z.npy` [1601]; `embed/gene_vectors.npy` [1601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1601 or target_col == 1601). Every well: [[ARHGAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
