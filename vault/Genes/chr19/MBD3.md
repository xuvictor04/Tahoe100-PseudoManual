---
symbol: "MBD3"
type: "gene"
col: 991
ensembl_id: "ENSG00000071655"
name: "methyl-CpG binding domain protein 3"
location: "19p13.3"
module: 5
arm: "+"
pooled_cpm: 21.26
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MBD3

*methyl-CpG binding domain protein 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +12.0, q 2e-30, up in 28 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +8.0, q 2e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.674× (z -6.8, q 6e-09, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASMTL-AS1]] (+0.67, fdr 7e-06), [[C1orf159]] (+0.67, fdr 7e-06), [[LINC00106]] (+0.67, fdr 1e-05); moves opposite to [[PRKAB2]] (-0.62, fdr 1e-05), [[LINC00888]] (-0.61, fdr 1e-05), [[PPDPF]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FAM229B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +12.0 | 2e-30 | 28/32 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.5 | 2e-28 | 39/44 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.0 | 2e-13 | 33/48 (NCI-H1792, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.7 | 2e-09 | 31/40 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.5 | 1e-08 | 31/44 (HT-29, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.3 | 1e-05 | 25/46 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.003 | 22/46 (LoVo, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.7 | 0.016 | 16/47 (A549, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +3.5 | 0.026 | 17/48 (A-172, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.026 | 18/44 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.026 | 18/45 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.21×** | +3.3 | 0.038 | 17/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.053 | 12/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.067 | 15/47 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +3.1 | 0.067 | 15/47 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.071 | 13/48 (A549, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -6.8 | 6e-09 | 29/47 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -4.4 | 0.003 | 21/47 (LoVo, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -3.6 | 0.063 | 20/47 (LS 180, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.767× | -3.2 | 0.17 | 14/48 (SHP-77, Hs 766T, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.781× | -3.0 | 0.30 | 21/47 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.8) |
| [[A-427 (line)]] | wt | 32.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +11.8) | — |
| [[A498 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.136× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.1) | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.2) |
| [[SW480 (line)]] | alt | 29.5 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL-AS1]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[C1orf159]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[LINC00106]] | +0.67 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[P2RY11]] | +0.65 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[EXOSC6]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ALG8]] | +0.63 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[GNL3L]] | +0.63 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[WDR4]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PUS1]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LETM1]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAB2]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[LINC00888]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PPDPF]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SNRNP48]] | -0.57 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[KBTBD3]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.55 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CAPN5]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[STAM2]] | -0.54 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[FAM229B]] | -0.54 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RAB11FIP1]] | -0.54 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[PJA2]] | -0.54 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CAT]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM229B]] | B | FAM229B activity raises MBD3's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without FAM229B | 0.060 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises MBD3's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without SLC16A1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[CREG2]] | B | CREG2 activity lowers MBD3's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.34× higher at baseline in the lines without CREG2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises MBD3's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without GBX2-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[LINC00888]] | B | LINC00888 activity raises MBD3's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without LINC00888 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -30.0); signed map (6.7, -52.9). **Vector** length 91.7, 21.1% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.5 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,573,596-1,592,865 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Methyl-CpG binding domain containing; NuRD complex subunits |
| Reactome | 31 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O95983](https://www.uniprot.org/uniprotkb/O95983) (Methyl-CpG-binding domain protein 3):

> Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Acts as transcriptional repressor and plays a role in gene silencing. Does not bind to methylated DNA by itself. Binds to a lesser degree DNA containing unmethylated CpG dinucleotides. Recruits histone deacetylases and DNA methyltransferases.

**Summary**, from NCBI Gene [53615](https://www.ncbi.nlm.nih.gov/gene/53615):

> DNA methylation is the major modification of eukaryotic genomes and plays an essential role in mammalian development. This gene belongs to a family of nuclear proteins which are characterized by the presence of a methyl-CpG binding domain (MBD). The encoded protein is a subunit of the NuRD, a multisubunit complex containing nucleosome remodeling and histone deacetylase activities. Unlike the other family members, the encoded protein is not capable of binding to methylated DNA. The protein …

**Accessions** — [HGNC:6918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6918) · Entrez [53615](https://www.ncbi.nlm.nih.gov/gene/53615) · UniProt [O95983](https://www.uniprot.org/uniprotkb/O95983) · Ensembl [ENSG00000071655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071655)

## Data

Gene col 991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 991); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 991]; `tensor/DDL_lfc|DDL_z.npy` [991]; `embed/gene_vectors.npy` [991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 991 or target_col == 991). Every well: [[MBD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
