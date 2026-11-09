---
symbol: "HPF1"
type: "gene"
col: 633
ensembl_id: "ENSG00000056050"
name: "histone PARylation factor 1"
location: "4q33"
module: 17
arm: "+"
pooled_cpm: 18.39
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# HPF1

*histone PARylation factor 1* — 4q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.16× (z +11.7, q 8e-29, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.78× (z +5.7, q 1e-06, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.431× (z -4.5, q 0.004, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCAF1]] (+0.75, fdr 7e-06), [[GPATCH11]] (+0.72, fdr 1e-05), [[FAM133B]] (+0.70, fdr 1e-05); moves opposite to [[LENG8-AS1]] (-0.67, fdr 3e-05), [[LY6G5B]] (-0.67, fdr 7e-06), [[HCG18]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CASC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.16×** | +11.7 | 8e-29 | 47/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.92×** | +10.9 | 3e-25 | 47/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.68×** | +10.0 | 3e-21 | 47/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +7.7 | 2e-12 | 37/43 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.81×** | +5.8 | 8e-07 | 34/47 (HEC-1-A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.7 | 1e-06 | 39/48 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +5.4 | 4e-06 | 36/48 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.43×** | +5.1 | 2e-05 | 28/47 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.66×** | +5.0 | 3e-05 | 27/42 (MIA PaCa-2, SNU-423, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.8 | 7e-05 | 30/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.52×** | +4.2 | 0.001 | 26/44 (Panc 03.27, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.004 | 26/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.52×** | +3.9 | 0.004 | 16/36 (A549, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.6 | 0.011 | 22/47 (C32, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.28×** | +3.5 | 0.016 | 17/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.039 | 15/48 (NCI-H1792, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +3.1 | 0.053 | 7/48 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.053 | 16/48 (AsPC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -4.5 | 0.004 | 27/45 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.4 | 0.004 | 26/47 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.549× | -3.2 | 0.27 | 16/46 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.567× | -3.0 | 0.33 | 12/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCAF1]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[GPATCH11]] | +0.72 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.70 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.67 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ATP5PO]] ⚠ | +0.66 | +0.42 / +0.66 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD2]] | +0.66 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[NUDT12]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ALAD]] | +0.64 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[METTL14]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[MTF2]] | +0.64 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[GEMIN2]] | +0.64 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[ISCA2]] | +0.63 | +0.34 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8-AS1]] | -0.67 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.67 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[HCG18]] | -0.64 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[NPIPB11]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.63 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.62 | -0.16 / -0.70 | ⚠ one half (not replicated) | 0.001 |  |
| [[GTF3C2-AS2]] | -0.62 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[SARM1]] | -0.62 | -0.24 / -0.58 | both halves | 4e-04 |  |
| [[LARP4B]] | -0.61 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.61 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[IL18BP]] | -0.61 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[ANKMY1]] | -0.60 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TIMM23B-AGAP6]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC11]] | B | CASC11 activity lowers HPF1's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without CASC11 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.0, -1.7); signed map (-20.7, -10.9). **Vector** length 72.4, 17.1% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.3 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | -3.6 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | histone PARylation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q33 — chr4:169,729,470-169,757,944 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20534; previously C4orf27 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWY4](https://www.uniprot.org/uniprotkb/Q9NWY4) (Histone PARylation factor 1):

> Cofactor for serine ADP-ribosylation that confers serine specificity on PARP1 and PARP2 and plays a key role in DNA damage response. Initiates the repair of double-strand DNA breaks: recruited to DNA damage sites by PARP1 and PARP2 and switches the amino acid specificity of PARP1 and PARP2 from aspartate or glutamate to serine residues, licensing serine ADP-ribosylation of target proteins. Serine ADP-ribosylation of target proteins, such as histones, promotes decompaction of chromatin and the …

**Summary**, from NCBI Gene [54969](https://www.ncbi.nlm.nih.gov/gene/54969):

> Enables chromatin binding activity; histone binding activity; and protein ADP-ribosyltransferase-substrate adaptor activity. Involved in DNA repair-dependent chromatin remodeling and double-strand break repair. Located in chromatin and nucleus. Is active in site of DNA damage. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26051) · Entrez [54969](https://www.ncbi.nlm.nih.gov/gene/54969) · UniProt [Q9NWY4](https://www.uniprot.org/uniprotkb/Q9NWY4) · Ensembl [ENSG00000056050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056050)

## Data

Gene col 633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 633); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 633]; `tensor/DDL_lfc|DDL_z.npy` [633]; `embed/gene_vectors.npy` [633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 633 or target_col == 633). Every well: [[HPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
