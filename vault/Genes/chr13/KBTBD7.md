---
symbol: "KBTBD7"
type: "gene"
col: 4208
ensembl_id: "ENSG00000120696"
name: "kelch repeat and BTB domain containing 7"
location: "13q14.11"
module: 12
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# KBTBD7

*kelch repeat and BTB domain containing 7* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +5.0, q 3e-04, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.311× (z -14.2, q 4e-43, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOK2]] (+0.76, fdr 7e-06), [[RP9]] (+0.74, fdr 7e-06), [[PEX12]] (+0.74, fdr 7e-06); moves opposite to [[CERS2]] (-0.66, fdr 7e-06), [[TTL]] (-0.63, fdr 1e-05), [[AKT1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-04 | 13/46 (A-172, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.7 | 6e-04 | 10/46 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.4 | 0.002 | 9/28 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.5 | 0.056 | 7/46 (Hs 766T, HEC-1-A, …) | top dose only | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.056 | 6/40 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.15 | 2/46 (SW480, MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.20 | 5/46 (SW480, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.311×** | -14.2 | 4e-43 | 35/45 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.418×** | -10.6 | 6e-24 | 32/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -10.2 | 2e-22 | 30/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -10.2 | 2e-22 | 27/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -6.4 | 2e-08 | 23/39 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -6.0 | 1e-07 | 14/36 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.608×** | -5.8 | 4e-07 | 14/28 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.780×** | -4.3 | 0.001 | 17/38 (Hs 766T, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.724×** | -3.9 | 0.006 | 14/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.710×** | -3.9 | 0.006 | 6/15 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -3.8 | 0.009 | 12/45 (HS-578T, Hs 766T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.028 | 5/45 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.034 | 13/46 (A-172, COLO 205, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.772×** | -3.1 | 0.066 | 11/45 (H4, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.39 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0842× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 4.62 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0763× (z -12.1) |
| [[A-172 (line)]] | wt | 7.68 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.264× (z -8.6) |
| [[PANC-1 (line)]] | alt | 5.45 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -8.8) |
| [[A-427 (line)]] | wt | 5.10 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0941× (z -8.8) |
| [[A498 (line)]] | wt | 7.31 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -10.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0455× (z -16.7) |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0605× (z -9.1) |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -14.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[J82 (line)]] | alt | 4.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 6.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0904× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0644× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0434× (z -10.1) |
| [[SNU-423 (line)]] | alt | 3.76 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0702× (z -8.8) |
| [[SW1417 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0801× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK2]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[RP9]] | +0.74 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[PEX12]] | +0.74 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.74 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 995 |
| [[ASB8]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[NUDT12]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PHAX]] | +0.69 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[BNIP1]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[GORAB]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | -0.66 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[TTL]] | -0.63 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[AKT1]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[IRAK1]] | -0.58 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[NFATC2IP]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZNF731P]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ATP11C]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KBTBD7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.6, -6.8); signed map (-15.0, -9.4). **Vector** length 58.7, 8.03% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,189,834-41,194,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434E2318 |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 8 pathways, smallest: Regulation of RAS by GAPs; Neddylation; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVZ9](https://www.uniprot.org/uniprotkb/Q8WVZ9) (Kelch repeat and BTB domain-containing protein 7):

> As part of the CUL3(KBTBD6/7) E3 ubiquitin ligase complex functions as a substrate adapter for the RAC1 guanine exchange factor (GEF) TIAM1, mediating its 'Lys-48' ubiquitination and proteasomal degradation. By controlling this ubiquitination, regulates RAC1 signal transduction and downstream biological processes including the organization of the cytoskeleton, cell migration and cell proliferation. Ubiquitination of TIAM1 requires the membrane-associated protein GABARAP which may restrict …

**Summary**, from NCBI Gene [84078](https://www.ncbi.nlm.nih.gov/gene/84078):

> The protein encoded by this gene is a transcriptional activator, having been shown to increase the transcription of activator protein-1 and serum response element. The encoded protein can also form a complex with KBTBD6 and CUL3, which regulates the ubiquitylation and degradation of TIAM1, which is a regulator of RAC1. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:25266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25266) · Entrez [84078](https://www.ncbi.nlm.nih.gov/gene/84078) · UniProt [Q8WVZ9](https://www.uniprot.org/uniprotkb/Q8WVZ9) · Ensembl [ENSG00000120696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120696)

## Data

Gene col 4208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4208); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4208]; `tensor/DDL_lfc|DDL_z.npy` [4208]; `embed/gene_vectors.npy` [4208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4208 or target_col == 4208). Every well: [[KBTBD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
