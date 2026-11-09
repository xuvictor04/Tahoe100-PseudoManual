---
symbol: "APOBEC3B"
type: "gene"
col: 11054
ensembl_id: "ENSG00000179750"
name: "apolipoprotein B mRNA editing enzyme catalytic subunit 3B"
location: "22q13.1"
module: 91
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# APOBEC3B

*apolipoprotein B mRNA editing enzyme catalytic subunit 3B* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +7.9, q 1e-12, up in 18 of 27 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.85× (z +4.1, q 0.003, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.554× (z -3.9, q 0.044, down in 13 of 31 measured lines) ⚠ cell-cycle shift, explains ~35% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0390×; ⚠ unreliable plate only); [[Omeprazole (drug)]] 0.5 µM in 1 line (A498 0.0637×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0957×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOBEC3A]] (+0.68, fdr 7e-06, ⚠ same locus), [[FAM111A]] (+0.67, fdr 1e-05), [[MSANTD7]] (+0.65, fdr 1e-05), [[HLA-H]] (+0.64, fdr 1e-05); moves opposite to [[TOMM20]] (-0.56, fdr 1e-05), [[EIF3CL]] (-0.52, fdr 5e-05), [[DUXAP10]] (-0.52, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOBEC3A]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Tucidinostat (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.29×** | +7.9 | 1e-12 | 18/27 (NCI-H2030, HepG2/C3A, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +7.5 | 2e-11 | 7/9 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +7.4 | 3e-11 | 2/3 (CFPAC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +7.0 | 4e-10 | 2/3 (A498, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.10×** | +4.8 | 2e-04 | 15/33 (LoVo, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.00×** | +4.7 | 3e-04 | 1/8 (SW1417) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +4.1 | 0.003 | 12/40 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +3.8 | 0.008 | 8/42 (BT-474, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.71×** | +3.5 | 0.030 | 1/13 (NCI-H1573) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.1 | 0.095 | 1/5 (NCI-H2347) | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.1 | 0.095 | 3/12 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.36× | +3.0 | 0.11 | 0/3 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.37× | +3.0 | 0.12 | 8/23 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0390×; ⚠ unreliable plate only); [[Omeprazole (drug)]] 0.5 µM in 1 line (A498 0.0637×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0957×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.554×** | -3.9 | 0.044 | 13/31 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.578× | -3.5 | 0.15 | 12/28 (KATO III, A498, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.611× | -3.3 | 0.19 | 7/39 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.637× | -3.0 | 0.36 | 10/39 (COLO 205, A-427, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.13 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0637× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 2.68 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0390× (z -9.3) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0957× (z -8.5) |
| [[A-172 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.823 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.558 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.581 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.574 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.670 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOBEC3A]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 | same gene group; pathway: Formation of the Editosome; STRING 939; ⚠ same locus (19.2 kb, same strand: neighbours can correlate without regulation) |
| [[FAM111A]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[MSANTD7]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[HLA-H]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RHNO1]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HASPIN]] | +0.61 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[C18orf54]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ZWINT]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RFX5]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZNF436]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[TMPO]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ZNF681]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[CXCL16]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM20]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[EIF3CL]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[DUXAP10]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TYW1]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BIRC6]] | -0.49 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[ZNF500]] | -0.48 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[MTDH]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF565]] | -0.48 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ACAP2]] | -0.48 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[RPL36A]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RBAK-RBAKDN]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[EIF3K]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3A]] | C | APOBEC3A activity raises APOBEC3B's level | lines that do not express APOBEC3A (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without APOBEC3A | 0.068 | ⚠ within organs, on part of the lines; also absent: PBX4, CTSV, APOBEC3B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tucidinostat (drug)]] 5 µM | C | APOBEC3B activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express APOBEC3B (3) vs lines expressing it (45) | the lines without APOBEC3B: 0.84× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: HSD3B7, KDELR3, HPS1 |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.1, -42.9); signed map (-43.8, -49.7). **Vector** length 52.6, 8.06% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | +3.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +0.9 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B mRNA editing enzyme catalytic subunit 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,982,347-38,992,804 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHRBNL, FLJ21201 |
| Gene groups (HGNC) | Apolipoprotein B mRNA editing enzyme catalytic subunits; Minor histocompatibility antigens |
| Reactome | 4 pathways, smallest: Formation of the Editosome; mRNA Editing: C to U Conversion; mRNA Editing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH17](https://www.uniprot.org/uniprotkb/Q9UH17) (DNA dC->dU-editing enzyme APOBEC-3B):

> DNA deaminase (cytidine deaminase) which acts as an inhibitor of retrovirus replication and retrotransposon mobility via deaminase-dependent and -independent mechanisms. After the penetration of retroviral nucleocapsids into target cells of infection and the initiation of reverse transcription, it can induce the conversion of cytosine to uracil in the minus-sense single-strand viral DNA, leading to G-to-A hypermutations in the subsequent plus-strand viral DNA. The resultant detrimental levels …

**Summary**, from NCBI Gene [9582](https://www.ncbi.nlm.nih.gov/gene/9582):

> This gene is a member of the cytidine deaminase gene family. It is one of seven related genes or pseudogenes found in a cluster, thought to result from gene duplication, on chromosome 22. Members of the cluster encode proteins that are structurally and functionally related to the C to U RNA-editing cytidine deaminase APOBEC1. It is thought that the proteins may be RNA editing enzymes and have roles in growth or cell cycle control. A hybrid gene results from the deletion of approximately 29.5 kb …

**Accessions** — [HGNC:17352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17352) · Entrez [9582](https://www.ncbi.nlm.nih.gov/gene/9582) · UniProt [Q9UH17](https://www.uniprot.org/uniprotkb/Q9UH17) · Ensembl [ENSG00000179750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179750)

## Data

Gene col 11054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11054); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11054]; `tensor/DDL_lfc|DDL_z.npy` [11054]; `embed/gene_vectors.npy` [11054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11054 or target_col == 11054). Every well: [[APOBEC3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOBEC3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
