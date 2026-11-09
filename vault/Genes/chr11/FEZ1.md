---
symbol: "FEZ1"
type: "gene"
col: 7388
ensembl_id: "ENSG00000149557"
name: "fasciculation and elongation protein zeta 1"
location: "11q24.2"
module: 75
arm: "+"
pooled_cpm: 6.1
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# FEZ1

*fasciculation and elongation protein zeta 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.67× (z +24.8, q 0e+00, up in 38 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Triamcinolone (drug)]] 0.05 µM in 1 line (Hs 766T 0.0698×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP6]] (+0.76, fdr 7e-06), [[LRRC8C-DT]] (+0.76, fdr 7e-06), [[SPATA21]] (+0.75, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.67×** | +24.8 | 0e+00 | 38/40 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +16.6 | 0e+00 | 29/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +14.5 | 3e-45 | 24/27 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +13.8 | 7e-41 | 11/11 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +12.6 | 4e-34 | 31/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +9.9 | 2e-21 | 14/16 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +9.9 | 3e-21 | 29/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +9.3 | 1e-18 | 28/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +8.7 | 2e-16 | 23/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +8.6 | 4e-16 | 24/38 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.7 | 7e-13 | 22/38 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +7.0 | 1e-10 | 15/32 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.9 | 3e-10 | 17/47 (A-427, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +6.0 | 8e-08 | 15/32 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 3e-06 | 18/46 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.2 | 8e-06 | 16/47 (A549, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.0 | 2e-05 | 19/47 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.9 | 3e-05 | 14/47 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.009 | 9/46 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.025 | 5/39 (A549, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Triamcinolone (drug)]] 0.05 µM in 1 line (Hs 766T 0.0698×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.786× | -3.2 | 0.36 | 13/46 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.36 | 5/45 (Panc 03.27, NCI-H1573, …) | two highest doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.849× | -3.1 | 0.36 | 6/47 (NCI-H1792, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.90 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 6.70 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +9.6) | [[Triamcinolone (drug)]] 0.05 µM 0.0698× (z -10.9) |
| [[KATO III (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +16.5) | — |
| [[NCI-H460 (line)]] | wt | 4.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.1) | — |
| [[A-172 (line)]] | wt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +9.2) | — |
| [[A498 (line)]] | wt | 2.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 3.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +8.6) | — |
| [[LoVo (line)]] | wt | 5.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +9.2) | — |
| [[A-427 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP6]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[LRRC8C-DT]] | +0.76 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.75 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.74 | +0.57 / +0.66 | both halves | 8e-06 |  |
| [[SLC27A6]] | +0.73 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.72 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.72 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[NPHS1]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FEZ1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APBB1]] | B | APBB1 activity raises FEZ1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without APBB1 | 0.091 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 24.2); signed map (37.1, 8.8). **Vector** length 59.1, 8.36% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +24.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.5 | +4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | fasciculation and elongation protein zeta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,442,881-125,592,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNC-76 |
| Gene groups (HGNC) | Fasciculation and elongation protein zeta family |
| Hallmark sets | APOPTOSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99689](https://www.uniprot.org/uniprotkb/Q99689) (Fasciculation and elongation protein zeta-1):

> May be involved in axonal outgrowth as component of the network of molecules that regulate cellular morphology and axon guidance machinery. Able to restore partial locomotion and axonal fasciculation to C.elegans unc-76 mutants in germline transformation experiments. May participate in the transport of mitochondria and other cargos along microtubules.

**Summary**, from NCBI Gene [9638](https://www.ncbi.nlm.nih.gov/gene/9638):

> This gene is an ortholog of the C. elegans unc-76 gene, which is necessary for normal axonal bundling and elongation within axon bundles. Expression of this gene in C. elegans unc-76 mutants can restore to the mutants partial locomotion and axonal fasciculation, suggesting that it also functions in axonal outgrowth. The N-terminal half of the gene product is highly acidic. Alternatively spliced transcript variants encoding different isoforms of this protein have been described. [provided by …

**Accessions** — [HGNC:3659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3659) · Entrez [9638](https://www.ncbi.nlm.nih.gov/gene/9638) · UniProt [Q99689](https://www.uniprot.org/uniprotkb/Q99689) · Ensembl [ENSG00000149557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149557)

## Data

Gene col 7388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7388); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7388]; `tensor/DDL_lfc|DDL_z.npy` [7388]; `embed/gene_vectors.npy` [7388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7388 or target_col == 7388). Every well: [[FEZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FEZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
