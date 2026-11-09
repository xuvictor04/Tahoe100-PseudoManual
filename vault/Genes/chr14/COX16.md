---
symbol: "COX16"
type: "gene"
col: 5492
ensembl_id: "ENSG00000133983"
name: "cytochrome c oxidase assembly factor COX16"
location: "14q24.2"
module: 178
arm: "+"
pooled_cpm: 98.37
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# COX16

*cytochrome c oxidase assembly factor COX16* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.98× (z +10.9, q 4e-25, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.638× (z -12.2, q 3e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.70, fdr 7e-06), [[NDUFB7]] (+0.69, fdr 7e-06), [[CWC15]] (+0.69, fdr 7e-06); moves opposite to [[NUP188]] (-0.60, fdr 7e-06), [[ELK4]] (-0.55, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +10.9 | 4e-25 | 46/49 (LS 180, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.5 | 3e-08 | 28/48 (Hs 766T, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +6.2 | 1e-07 | 34/48 (LS 180, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.9 | 7e-07 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 4e-05 | 35/48 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.6 | 4e-04 | 29/48 (LoVo, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.001 | 27/48 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.2 | 0.002 | 26/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.002 | 29/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.003 | 26/47 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.013 | 23/48 (HOP62, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.6 | 0.015 | 22/48 (SW48, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.6 | 0.015 | 21/38 (SK-MEL-2, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.017 | 22/45 (RKO, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.017 | 26/49 (H4, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.019 | 22/48 (AN3 CA, SHP-77, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.022 | 19/48 (A498, SHP-77, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.024 | 23/49 (J82, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.024 | 19/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.024 | 15/48 (HOP62, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -12.2 | 3e-31 | 40/48 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.795×** | -4.2 | 0.007 | 28/48 (COLO 205, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.021 | 26/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.836× | -3.3 | 0.12 | 20/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.893× | -3.0 | 0.27 | 4/48 (C-33 A, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 87.2 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.19× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.3) |
| [[C32 (line)]] | wt | 84.0 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 6.45× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.4) |
| [[COLO 205 (line)]] | alt | 193 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.9) |
| [[HOP62 (line)]] | alt | 72.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.32× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.1) |
| [[LS 180 (line)]] | wt | 128 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.72× (z +10.7) | — |
| [[RKO (line)]] | wt | 95.7 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.38× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) |
| [[A-172 (line)]] | wt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.0) |
| [[A498 (line)]] | wt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -9.9) |
| [[HS-578T (line)]] | alt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.6) |
| [[HT-29 (line)]] | alt | 56.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.41× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -16.1) |
| [[J82 (line)]] | alt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -8.9) |
| [[KATO III (line)]] | alt | 94.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.4) |
| [[LoVo (line)]] | wt | 97.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 72.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.45× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -9.9) |
| [[PANC-1 (line)]] | alt | 67.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.53× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 69.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.5) |
| [[SW 1271 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW 900 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -10.4) |
| [[SW48 (line)]] | wt | 67.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.89× (z +10.3) | — |
| [[SW480 (line)]] | alt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.62× (z +8.9) | — |
| [[A549 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[CWC15]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MED6]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[USPL1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SDHB]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[UBOX5]] | +0.63 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ING4]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ZNF461]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TENT2]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.60 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[ELK4]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.7, -16.3); signed map (-33.2, -10.7). **Vector** length 125, 36.7% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.2 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +9.6 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.8 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.6 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.4 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,325,081-70,416,984 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC203; previously C14orf112 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0S2](https://www.uniprot.org/uniprotkb/Q9P0S2) (Cytochrome c oxidase assembly protein COX16 homolog, mitochondrial):

> Required for the assembly of the mitochondrial respiratory chain complex IV (CIV), also known as cytochrome c oxidase. Promotes the insertion of copper into the active site of cytochrome c oxidase subunit II (MT-CO2/COX2). Interacts specifically with newly synthesized MT-CO2/COX and its copper center-forming metallochaperones SCO1, SCO2 and COA6. Probably facilitates MT-CO2/COX2 association with the MITRAC assembly intermediate containing MT-CO1/COX1, thereby participating in merging the …

**Summary**, from NCBI Gene [51241](https://www.ncbi.nlm.nih.gov/gene/51241):

> Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrial inner membrane. Implicated in mitochondrial complex IV deficiency nuclear type 22. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20213) · Entrez [51241](https://www.ncbi.nlm.nih.gov/gene/51241) · UniProt [Q9P0S2](https://www.uniprot.org/uniprotkb/Q9P0S2) · Ensembl [ENSG00000133983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133983)

## Data

Gene col 5492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5492); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5492]; `tensor/DDL_lfc|DDL_z.npy` [5492]; `embed/gene_vectors.npy` [5492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5492 or target_col == 5492). Every well: [[COX16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
