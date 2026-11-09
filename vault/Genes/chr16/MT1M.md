---
symbol: "MT1M"
type: "gene"
col: 12974
ensembl_id: "ENSG00000205364"
name: "metallothionein 1M"
location: "16q13"
module: 98
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 21
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# MT1M

*metallothionein 1M* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.54× (z +8.0, q 6e-13, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Chlorhexidine (diacetate) (drug)]] 5 µM: 4.54× (z +7.6, q 9e-12, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Lucanthone (drug)]] 0.05 µM: 0.326× (z -3.8, q 0.098, down in 3 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (J82 0.0537×; ⚠ cell-cycle shift, explains ~70% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.0287×; ⚠ cell-cycle shift, explains ~13% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1E]] (+0.80, fdr 7e-06, ⚠ read-through risk), [[MT1F]] (+0.79, fdr 7e-06, ⚠ same locus), [[TLR2]] (+0.73, fdr 7e-06), [[BATF]] (+0.73, fdr 7e-06), [[IRX3]] (+0.72, fdr 7e-06); moves opposite to [[MANCR]] (-0.53, fdr 1e-05), [[ADAM19]] (-0.53, fdr 1e-05), [[ASPH]] (-0.52, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MT1E]] → it (grade C ⚠); 5 go from it, the strongest it → [[MMP14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.54×** | +8.0 | 6e-13 | 4/6 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **4.54×** | +7.6 | 9e-12 | 15/16 (PANC-1, Hs 766T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.7×** | +6.8 | 2e-09 | 2/3 (J82, Hs 766T) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +6.6 | 8e-09 | 5/11 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.14×** | +6.0 | 3e-07 | 2/5 (Hs 766T, PANC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.37×** | +4.3 | 0.001 | 1/16 (J82) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.36×** | +4.3 | 0.001 | 6/11 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.17×** | +4.1 | 0.003 | 2/7 (CFPAC-1, PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.85×** | +3.7 | 0.013 | 2/8 (RKO, J82) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.79×** | +3.6 | 0.016 | 9/13 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.00×** | +3.4 | 0.031 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **2.62×** | +3.4 | 0.031 | 12/15 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.53×** | +3.3 | 0.044 | 7/12 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.51×** | +3.3 | 0.044 | 4/8 (RKO, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.51×** | +3.2 | 0.044 | 2/8 (J82, PANC-1) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.63×** | +3.2 | 0.053 | 4/8 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.30×** | +2.9 | 0.097 | 7/13 (Hs 766T, NCI-H1792, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (J82 0.0537×; ⚠ cell-cycle shift, explains ~70% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.0287×; ⚠ cell-cycle shift, explains ~13% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | **0.326×** | -3.8 | 0.098 | 3/17 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.408× | -3.0 | 0.46 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.0537× (z -8.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[PANC-1 (line)]] | alt | 1.62 | 1 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 12.9× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.0287× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-172 (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.110 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.116 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.109 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.146 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.132 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.170 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.126 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.153 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.562 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.128 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.133 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.589 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.116 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.661 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.0968 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.128 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.131 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.169 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.289 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1E]] | +0.80 | +0.81 / +0.81 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 853; ⚠ **readthrough risk**: this gene lies 5.5 kb 3′ of MT1E on the same strand (can correlate by spillover, not regulation) |
| [[MT1F]] | +0.79 | +0.75 / +0.85 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 858; ⚠ same locus (23.8 kb, same strand: neighbours can correlate without regulation) |
| [[TLR2]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[BATF]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[IRX3]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CEBPB]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[IRS2]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SAA1]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[MAOA]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MAFB]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANCR]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ADAM19]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ASPH]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ANXA10]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[IGFBP3]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[FAM227A]] | -0.49 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PSMD2]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PKIA]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1E]] | C | MT1E activity raises MT1M's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without MT1E | 0.032 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP14]] | B | MT1M activity raises MMP14's level | lines that do not express MT1M (29) vs lines expressing it (21) | 2.07× lower at baseline in the lines without MT1M | 0.061 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2 |
| [[SLC5A3]] | B | MT1M activity raises SLC5A3's level | lines that do not express MT1M (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without MT1M | 0.062 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2 |
| [[MT1E]] | C | MT1M activity raises MT1E's level | lines that do not express MT1M (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without MT1M | 0.002 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2; co-absent with the target |
| [[IRAK3]] | C | MT1M activity raises IRAK3's level | lines that do not express MT1M (29) vs lines expressing it (21) | 3.33× lower at baseline in the lines without MT1M | 0.046 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2; co-absent with the target |
| [[TLR2]] | C | MT1M activity raises TLR2's level | lines that do not express MT1M (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without MT1M | 0.076 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.7, 14.4); signed map (16.0, 30.5). **Vector** length 39.0, 11.3% of its response variance represented; |z| ≥ 3 in 296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | +3.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.8 | +1.8 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.8 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,632,659-56,633,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MT1, MT1K |
| Gene groups (HGNC) | Metallothioneins |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N339](https://www.uniprot.org/uniprotkb/Q8N339) (Metallothionein-1M):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4499](https://www.ncbi.nlm.nih.gov/gene/4499):

> This gene encodes a member of the metallothionein superfamily, type 1 family. Metallothioneins have a high content of cysteine residues that bind various heavy metals. These genes are transcriptionally regulated by both heavy metals and glucocorticoids. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:14296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14296) · Entrez [4499](https://www.ncbi.nlm.nih.gov/gene/4499) · UniProt [Q8N339](https://www.uniprot.org/uniprotkb/Q8N339) · Ensembl [ENSG00000205364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205364)

## Data

Gene col 12974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12974); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12974]; `tensor/DDL_lfc|DDL_z.npy` [12974]; `embed/gene_vectors.npy` [12974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12974 or target_col == 12974). Every well: [[MT1M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
