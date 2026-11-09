---
symbol: "ATF4"
type: "gene"
col: 4869
ensembl_id: "ENSG00000128272"
name: "activating transcription factor 4"
location: "22q13.1"
module: 29
arm: "-"
pooled_cpm: 194.36
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029", "written"]
generated_by: "tahoemap"
---

# ATF4

*activating transcription factor 4* — 22q13.1

> [!summary] In one line
> ATF4 is the bZIP transcription factor at the output end of the integrated stress response, translated preferentially when eIF2α is phosphorylated.

## What it is

Four kinases — PERK, GCN2, HRI and PKR — respond to ER stress, amino acid scarcity, haem or mitochondrial defects and oxidative stress by phosphorylating eIF2α. That lowers general initiation but raises translation of ATF4 specifically, through upstream open reading frames in its 5′ leader that ribosomes bypass only under stress. ATF4 then dimerises with other bZIPs at CARE/CRE-like elements and turns on amino acid transporters, aminoacyl-tRNA synthetases, one-carbon and serine synthesis genes, [[ATF3]], CHOP and [[GDF15]]. The programme is adaptive at first and lethal if the stress persists.

## What is uncertain

ATF4's regulation is translational, so its own mRNA level is a poor proxy for its activity — its transcript and the activity inferred from its targets measure different things. Which genes are ATF4's direct targets rather than CHOP's or ATF3's is not cleanly resolved, and the adaptive-versus-lethal split depends on stress duration in ways a single timepoint cannot separate. Where ATF4 and p53 share a target, attribution from expression alone is not possible.

## References

- Harding et al., 2000, Molecular Cell — regulated translation initiation controls stress-induced gene expression through ATF4.
- Vattem and Wek, 2004, PNAS — upstream open reading frames direct ATF4 translational control.
- Harding et al., 2003, Molecular Cell — defined the integrated stress response governing amino acid metabolism and oxidative stress resistance.
- Han et al., 2013, Nature Cell Biology — ATF4 and CHOP drive protein synthesis and ATP depletion toward cell death.
- Pakos-Zebrucka et al., 2016, EMBO Reports — review of the integrated stress response.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +10.9, q 9e-25, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.77× (z +9.4, q 2e-18, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG32]] (+0.76, fdr 7e-06), [[NPIPP1]] (+0.74, fdr 7e-06), [[SNHG8]] (+0.73, fdr 7e-06); moves opposite to [[BANF1]] (-0.72, fdr 7e-06), [[FKBP1A]] (-0.69, fdr 7e-06), [[ARF3]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCDHB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.23×** | +10.9 | 9e-25 | 46/48 (AsPC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.77×** | +9.4 | 2e-18 | 48/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +9.2 | 7e-18 | 46/48 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.41×** | +8.4 | 5e-15 | 48/48 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +5.4 | 7e-06 | 46/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.3 | 0.002 | 42/47 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 0.002 | 45/48 (NCI-H2030, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.9 | 0.008 | 37/48 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.008 | 37/48 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.47×** | +3.7 | 0.013 | 37/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.016 | 41/47 (NCI-H23, C32, …) | all doses, stronger at high dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.016 | 36/48 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.022 | 45/48 (RKO, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.022 | 36/49 (KATO III, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.029 | 36/47 (H4, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 30/48 (SK-MEL-2, C32, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 30/48 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.046 | 38/48 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.091 | 34/47 (AsPC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.788× | -3.3 | 0.16 | 27/48 (A-427, J82, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.706× | -3.2 | 0.16 | 28/48 (HS-578T, A498, …) | top dose only |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.795× | -3.2 | 0.16 | 39/48 (hTERT-HPNE, SW480, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.798× | -3.1 | 0.16 | 28/48 (A-427, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.712× | -3.1 | 0.16 | 34/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.726× | -3.1 | 0.16 | 31/48 (NCI-H2030, BT-474, …) | rises with dose | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.799× | -3.1 | 0.16 | 38/48 (hTERT-HPNE, Panc 03.27, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.801× | -3.1 | 0.16 | 28/49 (A498, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 162 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +22.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.36× (z +16.3) | — |
| [[C32 (line)]] | wt | 155 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +20.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.64× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 165 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.20× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 143 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.18× (z +9.4) | — |
| [[A498 (line)]] | wt | 218 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 197 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +16.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.19× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 143 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 185 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 249 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.99× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 274 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 152 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.31× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 183 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.02× (z +10.0) | — |
| [[RKO (line)]] | wt | 205 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.18× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 132 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.17× (z +9.6) | — |
| [[J82 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[KATO III (line)]] | alt | 288 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.8) | — |
| [[LoVo (line)]] | wt | 288 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.40× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 216 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.58× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 137 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.89× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 195 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.35× (z +9.9) | — |
| [[SW48 (line)]] | wt | 199 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +8.5) | — |
| [[SW480 (line)]] | alt | 193 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.79× (z +9.2) | — |
| [[A549 (line)]] | wt | 190 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HepG2_C3A (line)]] | wt | 218 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.06× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 199 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 269 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 179 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SNU-1 (line)]] | wt | 271 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.07× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 187 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 304 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 255 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 205 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG32]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[NPIPP1]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[EIF1]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 | STRING 470 |
| [[NFKBIL1]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[AK6]] | +0.70 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SNHG12]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BANF1]] | -0.72 | -0.73 / -0.61 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[FKBP1A]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[ARF3]] | -0.69 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[PPT1]] | -0.68 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.68 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[FKBP9]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[SELENON]] | -0.67 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[CHID1]] | -0.67 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[ELAVL1]] | -0.67 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[CDK2]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[PPP2R1B]] | -0.66 | -0.59 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHB2]] | B | PCDHB2 activity raises ATF4's level | lines that do not express PCDHB2 (22) vs lines expressing it (28) | 1.12× lower at baseline in the lines without PCDHB2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, VCAN, IHO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.8, -29.3); signed map (-5.9, -7.9). **Vector** length 138, 58.9% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.9 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.9 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.5 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.5 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.3 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Adenine (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,519,695-39,522,683 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAXREB67, CREB-2; previously TXREB |
| Gene groups (HGNC) | Activating transcription factor 4 family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 15 pathways, smallest: NFE2L2 regulating ER-stress associated genes; ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [P18848](https://www.uniprot.org/uniprotkb/P18848) (Cyclic AMP-dependent transcription factor ATF-4):

> Transcription factor that binds the cAMP response element (CRE) (consensus: 5'-GTGACGT[AC][AG]-3') and displays two biological functions, as regulator of metabolic and redox processes under normal cellular conditions, and as master transcription factor during integrated stress response (ISR). Binds to asymmetric CRE's as a heterodimer and to palindromic CRE's as a homodimer (By similarity). Core effector of the ISR, which is required for adaptation to various stress such as endoplasmic …

**Summary**, from NCBI Gene [468](https://www.ncbi.nlm.nih.gov/gene/468):

> This gene encodes a transcription factor that was originally identified as a widely expressed mammalian DNA binding protein that could bind a tax-responsive enhancer element in the LTR of HTLV-1. The encoded protein was also isolated and characterized as the cAMP-response element binding protein 2 (CREB-2). The protein encoded by this gene belongs to a family of DNA-binding proteins that includes the AP-1 family of transcription factors, cAMP-response element binding proteins (CREBs) and …

**Accessions** — [HGNC:786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:786) · Entrez [468](https://www.ncbi.nlm.nih.gov/gene/468) · UniProt [P18848](https://www.uniprot.org/uniprotkb/P18848) · Ensembl [ENSG00000128272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128272)

## Data

Gene col 4869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4869); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4869]; `tensor/DDL_lfc|DDL_z.npy` [4869]; `embed/gene_vectors.npy` [4869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4869 or target_col == 4869). Every well: [[ATF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ATF4.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
